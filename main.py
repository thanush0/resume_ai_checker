# main.py
import streamlit as st
from parser.extract_resume import extract_resume
from model.scorer import generate_report

st.title("🧠 AI Resume Screening System")

resume_file = st.file_uploader("Upload Resume (.pdf/.docx)", type=["pdf", "docx"])
jd = st.text_area("Paste Job Description")

if resume_file and jd:
    with open(f"temp/{resume_file.name}", "wb") as f:
        f.write(resume_file.read())

    text = extract_resume(f"temp/{resume_file.name}")
    report = generate_report(resume_file.name, text, jd)

    st.subheader("📊 Candidate Report")
    st.write(f"**Name:** {report['name']}")
    st.write(f"**Score:** {report['score']} / 100")
    st.write(f"**Recommendation:** {report['recommendation']}")
