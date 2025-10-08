from langchain_community.llms import Ollama
from langchain.prompts import PromptTemplate
from langchain_community.vectorstores import Chroma
from langchain_community.embeddings import OllamaEmbeddings
from langchain.chains import LLMChain
from utils.config import OLLAMA_MODEL, OLLAMA_URL, CHROMA_DB_DIR

def build_rag_evaluator_chain():
    llm = Ollama(model=OLLAMA_MODEL, base_url=OLLAMA_URL)
    embeddings = OllamaEmbeddings(model="nomic-embed-text", base_url=OLLAMA_URL)
    db = Chroma(persist_directory=CHROMA_DB_DIR, embedding_function=embeddings)

    template = """
You are a startup evaluator with access to previous startup ideas.

User's Idea:
{idea}

Retrieved Similar Ideas:
{context}

Compare the user's idea against the retrieved ones and evaluate:

1. Novelty & differentiation
2. Market potential
3. Technical feasibility
4. Strengths
5. Weaknesses or risks
6. Suggestions for improvement
7. Final verdict with score (out of 10)
"""

    prompt = PromptTemplate.from_template(template)
    chain = LLMChain(prompt=prompt, llm=llm)

    def evaluate(idea):
        docs = db.similarity_search(idea, k=3)
        context = "\n\n".join([d.page_content for d in docs])
        return chain.run({"idea": idea, "context": context})

    return evaluate
