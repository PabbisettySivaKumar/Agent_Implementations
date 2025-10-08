import os, uuid, pdfplumber
from dotenv import load_dotenv
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain.vectorstores import Chroma
from doc_uploader.embeddings import NomicOllamaEmbeddings
from graphdb.neo4j_setup import run_cypher

load_dotenv()
CHROMA_PERSIST_DIR = os.getenv("CHROMA_PERSIST_DIR", "./data/chroma_db")

def extract_text_from_pdf(path: str):
    text = []
    with pdfplumber.open(path) as pdf:
        for p in pdf.pages:
            t = p.extract_text()
            if t:
                text.append(t)
    return "\n".join(text)

def split_text(text: str):
    return RecursiveCharacterTextSplitter(chunk_size=1500, chunk_overlap=200).split_text(text)

def ingest_pdf_to_chroma(pdf_path: str, title: str):
    resource_id = str(uuid.uuid4())
    text = extract_text_from_pdf(pdf_path)
    chunks = split_text(text)
    embeddings = NomicOllamaEmbeddings()

    store = Chroma.from_texts(
        texts=chunks,
        embedding=embeddings,
        metadatas=[{"resource_id": resource_id, "title": title}],
        persist_directory=CHROMA_PERSIST_DIR
    )
    store.persist()

    run_cypher("MERGE (r:Resource {id:$id}) SET r.title=$title", {"id": resource_id, "title": title})
    return len(chunks)
