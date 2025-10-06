import sys, os
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

import streamlit as st
from chains.tutor_chains import build_tutor_chain

st.set_page_config(page_title="AI Tutor with Memory", layout="wide")
st.title("AI Tutor (LangChain + Ollama + Chroma)")

# Initialize the chain
if "chain" not in st.session_state:
    st.session_state.chain = build_tutor_chain()

if "chat_history" not in st.session_state:
    st.session_state.chat_history = []

question = st.text_area("Ask your question:")

if st.button("Ask"):
    if question.strip():
        with st.spinner("Thinking..."):
            response = st.session_state.chain({"question": question})
            answer = response.get("answer") or response.get("result") or "No response."
            st.session_state.chat_history.append((question, answer))
        st.markdown("### Answer")
        st.write(answer)
    else:
        st.warning("Please enter a question.")

if st.session_state.chat_history:
    st.markdown("---")
    st.markdown("### Chat Memory")
    for q, a in st.session_state.chat_history[-10:]:
        st.write(f"**Q:** {q}")
        st.write(f"**A:** {a}")
