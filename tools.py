from langchain.tools import tool
from langchain_google_genai.chat_models import ChatGoogleGenerativeAI
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from bs4 import BeautifulSoup
import requests
from pydantic import BaseModel
from dotenv import load_dotenv
load_dotenv()

@tool(name_or_callable="NbConverter")
def nb_convert(doc_dict):
    """ Creates a jupyter notebook that revises the whole documentation.

    Args:
        doc_dict: Dictionary where key is the page heading and value is another dictionary where key is the cell order number and value is a tuple with page content and content type if it is a Markdown or code.
    Returns:
        Creates a jupyter notebook file on local system.
    """

@tool(name_or_callable="DocUnderstanding")
def doc_analyser(doc_dict):
    """ Maps each page to it's content in sequenced form distinguishing if the content is markdown or code.

    Args:
        doc_dict: Dictionary where key is the page heading and value is the page content in Markdown form.
    Returns:
        dict: Returns dictionary where key is the page heading while value is another dictionary where key is order number and value is a tuple of format : ("content",code or markdown)
    """

@tool(name_or_callable="ContentPrettifier")
def content_prettifier(doc_dict:dict) -> str:
    """Prettifies the document content by converting it to markdown format

    Args:
        doc_dict: Dictionary where key is the page heading and value is the page content.
    Returns:
        dict: Returns a dictionary where key is the page heading and value is the prettified page content in markdown format.
    """
    content = '\n\n'.join(doc_dict.values())
    model = ChatGoogleGenerativeAI(model="gemini-2.5-flash")
    str_parser = StrOutputParser()
    prompt = PromptTemplate(
        template="""
        You are an expert in converting a documentation page content in well structured Markdown format without cutting off any information.
        Convert the following content to markdown:
        {content}
        
        Note: Do not truncate or delete any information.
        
        # Only return the final markdown text and nothing else.
        """,input_variables=["content"]
    )
    chain = prompt | model | str_parser
    
    chain.invoke({"content":doc})
    

@tool(name_or_callable="ContentFetcher")
def content_fetcher(docs: list[str],base_url: str) -> dict:
    """Fetches the content of the list of pages.

    Args:
        docs: List of all the pages whose text is to be extracted.
        base_url: The base url of documentation by which navigation to other pages is done.
    Returns:
        dict: Returns dictionary where key is the page heading while value is extracted page content.
    """
    doc_contents = {}
    
    for doc in docs:
        url = f"{base_url}/{doc}"
        response = requests.get(url)


        if response.status_code == 200:

            soup = BeautifulSoup(response.text, 'html.parser')
            

            content_div = soup.find('div', id=lambda x: x in ['content-area', 'content-container'] if x else False)
            if content_div:

                text = content_div.get_text(separator='\n', strip=True)
                doc_contents[doc] = text
            else:
                return "Content not found."
        else:
            return f"Failed to retrieve page. Status code: {response.status_code}"
    print(doc_contents)
    return doc_contents