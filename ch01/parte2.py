from langchain_ollama import ChatOllama
from langchain_core.prompts import PromptTemplate

llm = ChatOllama(
    model="llama3.1:8b",
    base_url="http://localhost:11434",  # opcional si es el default
    temperature=0.7,
)


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
    """You are an experienced copywriter. Escribe en castellano una redacccion de  {num_words} palabras 
sobr eel isugiente texto {text} usnado un tono {tone}"""
)

prompt_input = prompt_template.format(
    text=segovia_aqueduct_text,
    num_words=20,
    tone="knowledgeable and engaging",
)
response = llm.invoke(prompt_input)
print(response.content)
