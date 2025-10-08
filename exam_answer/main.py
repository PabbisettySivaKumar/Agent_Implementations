import streamlit as st
from dotenv import load_dotenv
import os

from agents.concept_clarity import concept_clarityAgent
from agents.completeness import CompletenessAgent
from agents.revisor import RevisorAgent

load_dotenv()

MODEL_NAME= os.getenv("MODEL_NAME")
TEMPERATURE= os.getenv("TEMPERATURE")

def revise_answer(question: str, answer: str):
    concept_clarity= concept_clarityAgent(MODEL_NAME, TEMPERATURE).evaluate(question, answer)
    completeness= CompletenessAgent(MODEL_NAME, TEMPERATURE).evaluate(question, answer)

    revisor= RevisorAgent(MODEL_NAME, TEMPERATURE)
    summary= revisor.summarize(question, answer, concept_clarity, completeness)

    return {
        "Concept & Clarity": concept_clarity,
        "Completeness": completeness,
        "Final Summary": summary
    }

#Streamlit

st.set_page_config(page_title= 'Exam Answer Revisor')
st.title('AI Powered Exam Answer Revisor')
st.markdown('Get instant Feedback of written Answer')

question= st.text_area('Enter the Question:')
answer= st.text_area('Enter your Answer:')

if st.button('Review my Answer'):
    if question.strip() and answer.strip():
        with st.spinner('Reviewing the Answer using AI Ollama Model'):
            results= revise_answer(question, answer)
        st.success('Revison Completed')

        for key, value in results.items():
            st.subheader(f'{key}')
            st.write(value)
    else:
        st.warning('Please Enter both question and answer before proceeding.')
st.markdown('---')
st.caption('Buitl with Lanchain Agents and Ollama Models')
