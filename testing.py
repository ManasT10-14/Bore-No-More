# import requests
# from bs4 import BeautifulSoup

# url = "https://docs.langchain.com/oss/python/langchain/overview" 


# response = requests.get(url)


# if response.status_code == 200:

#     soup = BeautifulSoup(response.text, 'html.parser')
    

#     content_div = soup.find('div', id='content-area')
    
#     if content_div:

#         text = content_div.get_text(separator='\n', strip=True)
#         print("----- Content from #content-area -----\n")
#         print(text)
#     else:
#         print("No div found with id='content-area'")
# else:
#     print(f"Failed to retrieve page. Status code: {response.status_code}")

[
    "install",
    "quickstart",
    "philosophy",
    "agents",
    "models",
    "messages",
    "tools",
    "short-term-memory",
    "streaming",
    "middleware",
    "structured-output",
    "guardrails",
    "runtime",
    "context-engineering",
    "mcp",
    "human-in-the-loop",
    "multi-agent",
    "retrieval",
    "long-term-memory",
    "studio",
    "test",
    "deploy",
    "ui",
    "observability"
]