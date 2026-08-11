from langchain_openai import ChatOpenAI
from dotenv import load_dotenv
import os
load_dotenv()
llm =ChatOpenAI(openai_api_key= os.getenv("ZAI_API_KEY"),openai_api_base="https://api.z.ai/api/paas/v4/",  # endpoint OpenAI-compatible de Z.AI
                model_name="glm-4.7-flash",temperature=0.7,)  
response = llm.invoke("hoy hace calor")
print(response.content)