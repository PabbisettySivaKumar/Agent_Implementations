import streamlit as st
from doc_uploader.pdfuploader import ingest_pdf_to_chroma
from agents.quiz_generator import generate_quiz
from progress.user_scores import record_user_score
import tempfile, json

st.set_page_config(page_title="AI Tutor", layout="centered")
st.title("AI Tutor")

st.write("Upload your study material (PDF), generate a short quiz, and check your score!")

user_name = st.text_input("Your Name")
uploaded_file = st.file_uploader("Upload PDF", type=["pdf"])
topic = st.text_input("Enter Topic (e.g. 'Photosynthesis')")
num_questions = st.slider("Number of Questions", 1, 10, 5)

if st.button("Generate Quiz"):
    if not uploaded_file or not topic:
        st.warning("Please upload a PDF and enter a topic.")
    else:
        with tempfile.NamedTemporaryFile(delete=False, suffix=".pdf") as tmp:
            tmp.write(uploaded_file.read())
            tmp.flush()
            ingest_pdf_to_chroma(tmp.name, uploaded_file.name)

        quiz_id, quiz = generate_quiz(topic, n=num_questions)
        st.session_state["quiz_id"] = quiz_id
        st.session_state["quiz"] = quiz
        st.session_state["answers"] = {}
        st.success(f"Quiz generated! ID: {quiz_id}")

if "quiz" in st.session_state:
    st.subheader("Take the Quiz")
    answers = {}
    for i, q in enumerate(st.session_state["quiz"], 1):
        st.markdown(f"**Q{i}. {q.get('question', 'No question text')}**")
        if q.get("options"):
            ans = st.radio("Choose:", q["options"], key=f"q_{i}")
        else:
            ans = st.text_input("Your answer:", key=f"q_{i}")

        user_ans = str(ans).strip().lower()
        correct_ans = str(q.get("answer", "")).strip().lower()

        answers[i] = {"ans": user_ans, "correct_ans": correct_ans, "correct": user_ans == correct_ans}

    if st.button("Submit"):
        total = len(answers)
        score = sum(1 for a in answers.values() if a["correct"])
        st.success(f"🎯 Your Score: {score}/{total}")
        if user_name:
            record_user_score(user_name, st.session_state["quiz_id"], score, total)
            st.info("Score saved in Neo4j.")
        else:
            st.warning("Enter your name to save score.")
