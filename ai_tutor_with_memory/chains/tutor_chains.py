from llms.ollama import get_ollama_model
from memory.chroma_memory import get_chroma_memory
from prompts.tutor_prompts import tutor_prompt
from langchain.chains import ConversationalRetrievalChain

def build_tutor_chain():
    llm = get_ollama_model()
    vectorstore, memory = get_chroma_memory()

    retriever = vectorstore.as_retriever(search_kwargs={"k": 3})

    chain = ConversationalRetrievalChain.from_llm(
        llm=llm,
        retriever=retriever,
        memory=memory,
        verbose=True
    )
    return chain
