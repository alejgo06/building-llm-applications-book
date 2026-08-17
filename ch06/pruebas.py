import chromadb
from llm_models import get_llm
from langchain_core.output_parsers import StrOutputParser
from typing import Dict, Any
from openai import OpenAI
from langchain_core.prompts import PromptTemplate
import argparse
def query_vector_database(question):
    chroma_client = chromadb.PersistentClient(path="./chroma_db")
    tourism_collection=chroma_client.get_collection(name="tourism_collection")
    results = tourism_collection.query(
        query_texts=[question],
        n_results=1
    )
    results_text = results['documents'][0][0]
    return results_text

# openai_client.chat
def prompt_template(question, text):
    return f'Use the following pieces of retrieved context to answer the question. Only use the retrieved context to answer the question. If you don\'t know the answer, or the answer is not contained in the retrieved context, just say that you don\'t know. Use three sentences maximum and keep the answer concise. \nQuestion: {question}\nContext: {text}. Remember: if you do not know, just say: I do not know. Do not make up an answer. For example do not say the three temples have got a total of three columns. \nAnswer:'

def execute_llm_prompt(prompt_input):
    openai_client = OpenAI(
    base_url="http://localhost:11434/v1",
    api_key="ollama",  # valor dummy, no se valida
    )
    prompt_response = openai_client.chat.completions.create(
        model="gemma4:e4b",
        messages=[
            {"role": "system", "content": "You are an assistant for question-answering tasks."},
            {"role": "user", "content": prompt_input}
        ])
    return prompt_response.choices[0].message.content
#end openai_client.chat

#langchain langchain_ollama langchain_openai
def execute_llmv2(question, text):
    PROMT="""
    Use the following pieces of retrieved context to answer the question. Only use the retrieved context to answer the question. 
    If you don\'t know the answer, or the answer is not contained in the retrieved context, just say that you don\'t know. Use three sentences maximum and keep the answer concise. 
    Question: {question}
    Context: {text}. 
    Remember: if you do not know, just say: I do not know. Do not make up an answer. For example do not say the three temples have got a total of three columns. \nAnswer:'
    """
    PROMPT_TEMPLATE = PromptTemplate.from_template(template=PROMT)


    prompt = PROMPT_TEMPLATE.format(
            question=question,
            text=text
        )
        
    # Get the LLM response
    llm = get_llm()
    response = llm.invoke(prompt)
    return response.content
    
#end langchain langchain_ollama langchain_openai




def run(question: str, call_type: str) -> str:
    context_text = query_vector_database(question)
 
    if call_type == "openai_client":
        prompt = prompt_template(question, context_text)
        return execute_llm_prompt(prompt)
    elif call_type == "langchain":
        return execute_llmv2(question, context_text)
    else:
        raise ValueError(f"Tipo de llamada no soportado: {call_type}")
    
def main():
    parser = argparse.ArgumentParser(
        description="Consulta la openai_client vectorial y responde con un LLM (Ollama vía OpenAI client o vía ChatOllama/get_llm)."
    )
    parser.add_argument(
        "-q", "--question",
        required=True,
        help="Pregunta a resolver, ej: 'How many columns have the three temples got in total?'",
    )
    parser.add_argument(
        "-t", "--type",
        choices=["openai_client", "langchain"],
        default="langchain",
        help="Tipo de llamada: 'openai_client' (OpenAI client -> execute_llm_prompt) o 'langchain' (get_llm -> execute_llmv2). Default: langchain",
    )
 
    args = parser.parse_args()
 
    answer = run(args.question, args.type)
    print(answer)
 
 
if __name__ == "__main__":
    main()