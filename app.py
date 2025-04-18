import streamlit as st
from utils.pdf_tools import extract_text_from_pdf, save_summary
from utils.summarizer import summarize_text

st.set_page_config(page_title="📚 PDF Notes Organizer")
st.title("📚 PDF Notes Organizer & Summarizer")

uploaded_files = st.file_uploader("Upload one or more PDF notes", type="pdf", accept_multiple_files=True)

if uploaded_files:
    for file in uploaded_files:
        st.markdown(f"---\n### 📄 File: `{file.name}`")
        text = extract_text_from_pdf(file)
        st.text_area("Extracted Text", text[:2000] + "...", height=200)
        
        if st.button(f"Summarize {file.name}"):
            with st.spinner("Summarizing..."):
                summary = summarize_text(text)
                save_summary(summary, filename=f"{file.name}_summary.txt")
                st.subheader("📝 Summary:")
                st.success(summary)
