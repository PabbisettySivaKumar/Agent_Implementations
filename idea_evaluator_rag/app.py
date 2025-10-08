import streamlit as st
from evaluator_chain import build_rag_evaluator_chain

st.set_page_config(page_title="RAG-Based Idea Evaluator", layout="wide")
st.title("RAG-Based Idea Evaluator (LangChain + Ollama + ChromaDB)")

st.write("""
Enter your startup idea below.  
The system retrieves similar ideas from a local database and evaluates it based on novelty, feasibility, and market potential.
""")

idea = st.text_area("Your Startup Idea", height=150,
                    placeholder="Example: An AI platform that predicts plant diseases from photos and gives organic treatment suggestions.")

if st.button("Evaluate Idea"):
    if not idea.strip():
        st.warning("Please enter an idea to evaluate.")
    else:
        with st.spinner("Evaluating your idea using RAG..."):
            evaluator = build_rag_evaluator_chain()
            result = evaluator(idea)

        st.success("Evaluation Complete!")
        st.markdown("### Evaluation Report")
        st.write(result)
