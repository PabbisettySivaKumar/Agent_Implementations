import streamlit as st
from orchestrator import startup_pitch_pipeline

st.set_page_config(page_title= "Start up Pitch Team", layout= "wide")
st.title("Start-Up Pitch Meeting Analyzer using Multi-Agent System")

st.write("This Application Helps in building a Pitch Deck")
idea= st.text_area("Enter Start-Up Idea: ", height= 150)

if st.button("Generate Pitch Deck"):
    if not idea.strip():
        st.warning("Enter your Idea")
    else:
        with st.spinner("Building your pitch...yo...wait, it take's time"):
            results= startup_pitch_pipeline(idea)
        st.success('Pitch Comoleted')

        st.markdown('### Idea Summary')
        st.write(results["idea_summary"])

        st.markdown('### Market Analysis')
        st.write(results["market"])

        st.markdown('### Financials')
        st.write(results["financials"])

        st.markdown('### Pitch')
        st.write(results["pitch"])