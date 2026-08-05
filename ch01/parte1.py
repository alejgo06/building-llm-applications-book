from langchain_ollama import ChatOllama
llm = ChatOllama(
    model="llama3.1:8b",
    base_url="http://localhost:11434",  # opcional si es el default
    temperature=0.7,
)

response = llm.invoke("hoy hace calor")
print(response.content)