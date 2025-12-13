from langchain_google_genai.chat_models import ChatGoogleGenerativeAI
from pydantic import BaseModel,Field
from langchain.tools import tool
from tools import content_fetcher,doc_analyser
from langchain.agents import create_agent
from prompts import system_prompt
from langchain.messages import HumanMessage
from dotenv import load_dotenv
from langgraph.graph import StateGraph,END,START
from langgraph.graph.message import add_messages
from nodes import ChatState
load_dotenv()

class ChatState(StateGraph):
    ai_msgs: list[str,add_messages]
    human_query: list[str,add_messages]

class BNM:
    def __init__(self):
        self.model = ChatGoogleGenerativeAI(model="gemini-2.5-flash")
    
    def llm_call(self,state:ChatState):
        query = state["human_query"][-1]
        result = self.llm_with_tools.invoke({"human_query":query})
        return {"ai_msgs":result.content}
    
    def create_graph(self):
        workflow = StateGraph(state_schema=ChatState)
        workflow.add_node()
        
    
if __name__=="__main__":
    obj = BNM()
    agent = obj.create_agent
    result = agent.invoke({"messages":[HumanMessage(content="for the documentation : https://docs.langchain.com/oss/python/langchain summarize me the pages: quickstart and philosophy and also return the prettified result.")]})
    
    