from langchain_ollama import ChatOllama
from langchain_core.prompts import PromptTemplate

llm = ChatOllama(
    model="llama3.1:8b",
    base_url="http://localhost:11434",  # opcional si es el default
    temperature=0.7,
)

prompt_input = """Classify the following numbers as Abra, Kadabra or Abra Kadabra:

3, 4, 5, 7, 8, 10, 11, 13, 35

Examples: 
6 // not divisible by 5, not divisible by 7 // None
15 // divisible by 5, not divisible by 7 // Abra
12 // not divisible by 5, not divisible by 7 // None
21 // not divisible by 5, divisible by 7 // Kadabra
70 // divisible by 5, divisible by 7 // Abra Kadabra
"""

response = llm.invoke(prompt_input)
print(response.content)