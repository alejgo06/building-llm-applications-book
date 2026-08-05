from langchain_ollama import ChatOllama
from langchain_core.prompts import PromptTemplate

llm = ChatOllama(
    model="llama3.1:8b",
    base_url="http://localhost:11434",  # opcional si es el default
    temperature=0.7,
)



                 
prompt_input = """Write a coincise message to remind users 
to be vigilant about phishing attacks."""

response = llm.invoke(prompt_input)
print(response.content)

