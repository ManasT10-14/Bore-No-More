from langchain_google_genai.chat_models import ChatGoogleGenerativeAI
from pydantic import BaseModel,Field
from langchain.tools import tool
from tools import content_fetcher
from langchain.agents import create_agent
from prompts import system_prompt
from langchain.messages import HumanMessage
from dotenv import load_dotenv
load_dotenv()
class BNM:
    def __init__(self):
        self.model = ChatGoogleGenerativeAI(model="gemini-2.5-flash")
        self.create_agent = create_agent(model=self.model,tools=[content_fetcher],system_prompt=system_prompt)
    
    
if __name__=="__main__":
    obj = BNM()
    agent = obj.create_agent
    result = agent.invoke({"messages":[HumanMessage(content="for the documentation : https://docs.langchain.com/oss/python/langchain summarize me the pages: quickstart and philosophy ")]})
    print(result)        
    