import streamlit as st
from openai import OpenAI
from typing import TypedDict
from pydantic import BaseModel
from langgraph.graph import StateGraph, START, END
from langchain_openai import ChatOpenAI
from langchain_core.messages import BaseMessage
from math_agent import MathAgent
from reading_agent import ReadingAgent
from writing_agent import WritingAgent
from smalltalk_agent import SmallTalkAgent
from clarify_agent import ClarifyAgent
from prompt_store import get_prompt
from create_llm_message import create_llm_msg

class AgentState(TypedDict):
    incrementalResponse: str
    lnode: str
    category: str
    message_history: list[BaseMessage]

class Category(BaseModel):
    category: str

VALID_CATEGORIES = ["smalltalk", "clarify", "math", "reading", "writing"]

class TeacherAgent():
    def __init__(self, api_key):
        self.model = ChatOpenAI(model=st.secrets['OPENAI_MODEL'], api_key=api_key)
        
        self.math_agent_class = MathAgent(self.model)
        self.reading_agent_class = ReadingAgent(self.model)
        self.writing_agent_class = WritingAgent(self.model)
        self.smalltalk_agent_class = SmallTalkAgent(self.model)
        self.clarify_agent_class = ClarifyAgent(self.model)

        workflow = StateGraph(AgentState)
        workflow.add_node("classifier", self.initial_classifier)
        workflow.add_node("math", self.math_agent_class.math_agent)
        workflow.add_node("reading", self.reading_agent_class.reading_agent)
        workflow.add_node("writing", self.writing_agent_class.writing_agent)
        workflow.add_node("smalltalk", self.smalltalk_agent_class.smalltalk_agent)
        workflow.add_node("clarify", self.clarify_agent_class.clarify_agent)

        workflow.add_conditional_edges("classifier", self.main_router)
        workflow.add_edge(START, "classifier")
        workflow.add_edge("smalltalk", END)
        workflow.add_edge("clarify", END)
        workflow.add_edge("math", END)
        workflow.add_edge("reading", END)
        workflow.add_edge("writing", END)

        self.graph = workflow.compile()

    def initial_classifier(self, state: AgentState):
        print("initial classifier")
        CLASSIFIER_PROMPT = get_prompt("classifier")
        llm_messages = create_llm_msg(CLASSIFIER_PROMPT, state["message_history"])
        llm_response = self.model.with_structured_output(Category).invoke(llm_messages)
        category = llm_response.category
        print(f"category is {category}")
        return {
            "lnode": "initial_classifier",
            "category": category,
        }
    
    def main_router(self, state: AgentState):
        my_category = state['category']
        if my_category in VALID_CATEGORIES:
            return my_category
        else:
            print(f"unknown category: {my_category}")
            return END