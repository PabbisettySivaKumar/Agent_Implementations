import streamlit as st
from orchestrator import build_itinerary

st.set_page_config(page_title="Travel Itinerary Builder", layout="wide")
st.title("AI Travel Itinerary Builder (Multi-Agent)")

st.write("Plan your next trip with the help of AI agents — fully offline using Ollama.")

destination = st.text_input("Destination or region:", "Bali")
duration = st.number_input("Duration (days):", min_value=1, max_value=30, value=5)
interests = st.text_area("Your interests (e.g., adventure, culture, beaches):", "beaches, food, nature")
budget = st.number_input("Approximate budget (USD):", min_value=100, max_value=10000, value=1500)

if st.button("Build My Itinerary"):
    with st.spinner("Building your itinerary..."):
        result = build_itinerary(destination, duration, interests, budget)

    st.success("Your AI-generated itinerary is ready!")

    st.markdown("### Destination Recommendations")
    st.write(result["destinations"])

    st.markdown("### Accommodation Suggestions")
    st.write(result["accommodation"])

    st.markdown("### Activities Plan")
    st.write(result["activities"])

    st.markdown("### Budget Overview")
    st.write(result["budget"])

    st.markdown("### Final Travel Itinerary")
    st.write(result["final_itinerary"])
