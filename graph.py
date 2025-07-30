import streamlit as st
from openai import OpenAI
from pydantic import BaseModel
from langchain_openai import ChatOpenAI

class AgentState(TypedDict):
    incrementalResponse: str
    lnode: str
    category: str
    message_history: list[BaseMessage]

class Category(BaseModel):
    category: str

VALID_CATEGORIES = ["math", "reading", "writing"]

class TeacherAgent():
    def __init__(self, api_key, embedding_model):
        self.client = OpenAI(api_key=api_key)
        self.model = ChatOpenAI(model=st.secrets['OPENAI_MODEL'], api_key=api_key)

        self.math_agent_class = MathAgent(self.client, self.model, self.index, embedding_model)
        