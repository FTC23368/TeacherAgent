import streamlit as st
from langchain_core.messages import BaseMessage
from create_llm_message import create_llm_msg
from prompt_store import get_prompt

class WritingAgent:
    def __init__(self, model):
        self.model = model

    def generate_response(self, message_history: list[BaseMessage]):
        user_query = message_history[-1].content
        writing_prompt = get_prompt("writing").format(user_query=user_query)
        llm_messages = create_llm_msg(writing_prompt, message_history)
        return self.model.stream(llm_messages)
    
    def writing_agent(self, state: dict) -> dict:
        return {
            "lnode": "writing_agent",
            "incrementalResponse": self.generate_response(state['message_history']),
            "category": "writing"
        }
