from langchain_core.prompts import ChatPromptTemplate
from langchain_core.chat_history import InMemoryChatMessageHistory
from langchain_chroma import Chroma
from langchain_ollama import OllamaEmbeddings
from langchain_core.prompts import PromptTemplate
from llm_models import get_llm
from langchain_core.runnables import RunnablePassthrough
import argparse
from langchain_core.runnables import RunnableLambda

from dotenv import load_dotenv
load_dotenv()

rag_prompt = ChatPromptTemplate.from_messages(
    [
        ("system", """You are a helpful assistant, world-class 
        expert in Roman and Greek history, especially in towns 
        located in southern Italy. Provide interesting insights 
        on local history and recommend places to visit with 
        knowledgeable and engaging answers. Answer all questions 
        to the best of your ability, but only use what has been 
        provided in the context. If you don't know, just say you 
        don't know. Use three sentences maximum and keep
        the answer as concise as possible."""),
        ("placeholder", "{chat_history_messages}"),
        ("assistant", "{retrieved_context}"),
        ("human", "{question}"),
    ]
)


chat_history_memory = InMemoryChatMessageHistory()


embeddings_model = OllamaEmbeddings(
    model="nomic-embed-text",
    base_url="http://localhost:11434",
)
vector_db = Chroma(
    collection_name="tourist_info",
    embedding_function=embeddings_model,
    persist_directory="./chroma_db",
)
retriever = vector_db.as_retriever(
        search_type="similarity",
        search_kwargs={"k": 5}
    )

def get_messages(x):
    return chat_history_memory.messages

def execute_chain_with_memory(chain, question,verbose=False):
    chat_history_memory.add_user_message(question)
    answer = chain.invoke(question,
                            config={"tags": ["rag-tourist-info"], "metadata": {"has_memory": True}}# se peude comentar 
                          )
    chat_history_memory.add_ai_message(answer)
    if verbose:
        print(f'Full chat message history: {chat_history_memory.messages}\n\n')
    return answer

llm = get_llm()

rag_chain = {"retrieved_context":retriever, 
             "question": RunnablePassthrough(),
             "chat_history_messages": RunnableLambda(get_messages),
             }|rag_prompt|llm

question='Where was Poseidonia and who renamed it to Paestum? Also tell me the source.'
print(question)
answer=execute_chain_with_memory(rag_chain, question)
print(answer.content) 


question = """And then what did they do? Also tell me the source"""
print(question)
answer=execute_chain_with_memory(rag_chain, question)
print(answer.content)    


question = """And then what did they do? Also tell me the source"""
print(question)
answer=execute_chain_with_memory(rag_chain, question)
print(answer.content)    