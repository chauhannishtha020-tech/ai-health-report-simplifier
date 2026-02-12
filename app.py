import streamlit as st
import google.generativeai as genai
import os

# API key
genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

# Model
model = genai.GenerativeModel("models/gemini-1.5-flash")

st.title("🩺 AI Health Report Simplifier")
st.write("Paste your health report and get a simple explanation.")

report_text = st.text_area("Paste your report here")

if st.button("Simplify"):
    if report_text.strip() == "":
        st.warning("Please paste your medical report.")
    else:
        prompt = f"""
        Explain the following medical report in very simple language.
        Use bullet points.
        Mention if values are normal or not.
        Do NOT give medical advice.

        Report:
        {report_text}
        """

        response = model.generate_content(prompt)
        st.subheader("Simplified Explanation")
        st.write(response.text)
