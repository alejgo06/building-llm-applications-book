from langchain_ollama import ChatOllama

# No hace falta API key. base_url por defecto es http://localhost:11434
llm = ChatOllama(
    model="llama3.1:8b",
    base_url="http://localhost:11434",  # opcional si es el default
    temperature=0.7,
)

response = llm.invoke("It's a hot day, I would like to go to the...")
print(response.content)

prompt_input = """Write a short message to remind users to be 
vigilant about phishing attacks."""
response = llm.invoke(prompt_input)
print(response.content)

from langchain_core.prompts import PromptTemplate

segovia_aqueduct_text = """The Aqueduct of Segovia 
(Spanish: Acueducto de Segovia) is a Roman aqueduct in Segovia, 
Spain. It was built around the first century AD to channel water 
from springs in the mountains 17 kilometres (11 mi) away to the 
city's fountains, public baths and private houses, and was in 
use until 1973. Its elevated section, with its complete arcade 
of 167 arches, is one of the best-preserved Roman aqueduct 
bridges and the foremost symbol of Segovia, as evidenced by 
its presence on the city's coat of arms. The Old Town of 
Segovia and the aqueduct, were declared a UNESCO World 
Heritage Site in 1985."""

prompt_template = PromptTemplate.from_template(
    """You are an experienced copywriter. Write a {num_words} words 
summary of the following text, using a {tone} tone: {text}"""
)

prompt_input = prompt_template.format(
    text=segovia_aqueduct_text,
    num_words=20,
    tone="knowledgeable and engaging",
)
response = llm.invoke(prompt_input)
print(response.content)

# Uso con chain (LCEL) — igual que con OpenAI
chain = prompt_template | llm
response = chain.invoke({
    "text": segovia_aqueduct_text,
    "num_words": 20,
    "tone": "knowledgeable and engaging",
})
print(response.content)