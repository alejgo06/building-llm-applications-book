from langchain_chroma import Chroma
from langchain_ollama import OllamaEmbeddings
from langchain_core.prompts import PromptTemplate
from llm_models import get_llm
from langchain_core.runnables import RunnablePassthrough
import argparse

def main():
    parser = argparse.ArgumentParser(
        description="Consulta la openai_client vectorial y responde con un LLM."
    )
    parser.add_argument(
        "-q", "--question",
        required=True,
        help="Pregunta a resolver, ej: 'Where was Poseidonia and who renamed it to Paestum. Also tell me the source'",
    )
 
    args = parser.parse_args()
    
    embeddings_model = OllamaEmbeddings(
    model="nomic-embed-text",
    base_url="http://localhost:11434",
    )

    vector_db = Chroma(
        collection_name="tourist_info",
        embedding_function=embeddings_model,
        persist_directory="./chroma_db",
    )


    rag_prompt_template = """Use the following pieces of context
    to answer the question at the end. 
    If you don't know the answer, just say that you don't know, 
    don't try to make up an answer.
    Use three sentences maximum and keep the 
    answer as concise as possible.
    {context}
    Question: {question}
    Helpful Answer:"""

    rag_prompt = PromptTemplate.from_template(rag_prompt_template)
    retriever = vector_db.as_retriever(
        search_type="similarity",
        search_kwargs={"k": 5}
    )
    

    llm = get_llm()

    rag_chain = {"context":retriever, 
             "question": RunnablePassthrough()}|rag_prompt|llm


    answer = rag_chain.invoke(args.question)
    print(answer.content)

 
 
if __name__ == "__main__":
    main()