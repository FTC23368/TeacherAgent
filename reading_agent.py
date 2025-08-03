from langchain_core.messages import BaseMessage
from create_llm_message import create_llm_msg
from prompt_store import get_prompt

class ReadingAgent:
    def __init__(self, model):
        self.model = model

    def generate_response(self, message_history: list[BaseMessage]):
        user_query = message_history[-1].content
        reading_prompt = get_prompt("reading").format(user_query=user_query)
        llm_messages = create_llm_msg(reading_prompt, message_history)
        return self.model.stream(llm_messages)
    
    def reading_agent(self, state: dict) -> dict:
        return {
            "lnode": "reading_agent",
            "incrementalResponse": self.generate_response(state['message_history']),
            "category": "reading"
        }
