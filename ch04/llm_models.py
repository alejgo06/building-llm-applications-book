from langchain_openai import ChatOpenAI
from langchain_ollama import ChatOllama
from dotenv import load_dotenv
import os

load_dotenv()

def get_llm(): 
    
    llm_provider  = os.getenv("LLM_PROVIDER", "local")

    if llm_provider =="local":
        return ChatOllama(model="llama3.1:8b",base_url="http://localhost:11434",
                          temperature=0.7,)
    elif llm_provider  == "gpt":
        return ChatOpenAI(openai_api_key=os.getenv("OPENAI_API_KEY"), 
                          model_name="gpt-5-nano")
    elif llm_provider  == "zai":
        return ChatOpenAI(openai_api_key=os.getenv("ZAI_API_KEY"),openai_api_base="https://api.z.ai/api/paas/v4/",  
                          model_name="glm-4.7-flash",
                          temperature=0.7,
        )
    


