import streamlit as st
import requests
import os
import json
from dotenv import load_dotenv

load_dotenv()

st.set_page_config(page_title="Exam Answer Revisor", page_icon="📚")
st.title("Exam Answer Revisor (AI Evaluator)")

# Input fields
question= st.text_area("Exam Question", placeholder="Enter the question...")
student_answer= st.text_area("Student Answer", placeholder="Paste the student's answer...")

# API endpoint
API_URL= os.getenv("API_URL")
API_KEY= os.getenv("LANGFLOW_API_KEY")

if st.button("Evaluate Answer"):
    if not question or not student_answer:
        st.warning("Please enter both the question and the student's answer.")
    elif not API_KEY:
        st.error("LANGFLOW_API_KEY not set. Please export it before running Streamlit.")
    else:
        # Prepare payload
        payload= {
            "input_type": "text",
            "output_type": "text",
            "input_value": f"Question: {question}\nStudent's Answer: {student_answer}"
        }

        headers= {
            "Content-Type": "application/json",
            "x-api-key": API_KEY
        }

        with st.spinner("Evaluating the answer..."):
            try:
                res = requests.post(API_URL, headers=headers, json=payload)
                res.raise_for_status()
                data = res.json()

                # Navigate nested structure safely
                output_text = (
                    data["outputs"][0]["outputs"][0]["results"]["text"]["data"]["text"]
                )

                # Try to parse the JSON output from model
                try:
                    result = json.loads(output_text)
                    st.subheader("Revised Answer")
                    st.write(result.get("revised_answer", ""))

                    st.subheader("Feedback")
                    st.info(result.get("feedback", ""))

                    st.subheader("Marks")
                    st.success(f"{result.get('marks', 'N/A')}/10")

                except json.JSONDecodeError:
                    st.warning("The output wasn't valid JSON. Showing raw text instead:")
                    st.text(output_text)

            except Exception as e:
                st.error(f"Error: {e}")
