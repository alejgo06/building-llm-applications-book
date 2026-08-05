from langchain_ollama import ChatOllama
from langchain_core.prompts import PromptTemplate

from openai import OpenAI

# Ollama expone un endpoint compatible con la API de OpenAI en /v1
# api_key es obligatorio para el SDK pero Ollama lo ignora — cualquier string vale
client = OpenAI(
    base_url="http://localhost:11434/v1",
    api_key="ollama",  # valor dummy, no se valida
)

prompt_input = """Write a coincise message to remind users 
to be vigilant about phishing attacks."""
response = client.chat.completions.create(
  model="llama3.1:8b",
  messages=[
    {"role": "system", "content": "You are a helpful assistant."},
    {"role": "user", "content": prompt_input}
  ] 
)

print(response)
print(response.choices[0].message.content)


