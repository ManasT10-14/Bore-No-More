from langchain_google_genai.chat_models import ChatGoogleGenerativeAI
from pydantic import BaseModel,Field
from langchain.tools import tool
import requests
from bs4 import BeautifulSoup
class Agent:
    def __init__(self):
        self.model = ChatGoogleGenerativeAI(model="gemini-2.5-flash")
        
    @tool(name_or_callable="NotebookGenerator")
    def nb_generator(self,content:str):
        pass
    
    @tool(name_or_callable="ContentGenerator")
    def content_generator(self,doc_address:str) -> str:
        pass
    
    @tool(name_or_callable="ContentFetcher")
    def content_fetcher(self,docs: list[str],base_url: str) -> str:
        """Fetches the content of the list of pages.

        Args:
            docs: List of all the pages whose text is to be extracted.
            base_url: The base url of documentation by which navigation to other pages is done.
        Returns:
            str: The combined content of all the pages.
        """
        doc_contents = ""
        
        for doc in docs:
            url = f"{base_url}/{doc}"
            response = requests.get(url)


            if response.status_code == 200:

                soup = BeautifulSoup(response.text, 'html.parser')
                

                content_div = soup.find('div', id=lambda x: x in ['content-area', 'content-container'] if x else False)
                if content_div:

                    text = content_div.get_text(separator='\n', strip=True)
                    doc_contents+=f"# {doc}\n{text}\n"
                else:
                    return "Content not found."
            else:
                return f"Failed to retrieve page. Status code: {response.status_code}"
        print(doc_contents)
        return doc_contents

            