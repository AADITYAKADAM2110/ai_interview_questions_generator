import streamlit as st
from main import main
from schemas.validator import validate_output

if __name__ == "__main__":
    st.title("AI Interview Questions Generator")
    st.write("Generate tailored interview questions and evaluation rubrics for any role and experience level.")
    
    st.subheader("Input Parameters")
    role = st.text_input("Job Role", placeholder="e.g., Software Engineer, Data Analyst, Product Manager")
    experience_level = st.selectbox("Experience Level", options=["Junior (0–1 years)", "Mid (2–4 years)", "Senior (4+ years)"])

    if st.button("Generate Interview Questions"):
        with st.spinner("Generating questions..."):
            try:
                output = main(role, experience_level)
                response = validate_output(output)
            except Exception as e:
                st.error(f"Failed to generate valid questions: {e}")
                response = None

            if response:
                st.write(response)

        st.markdown("---")

        if response:
            st.download_button(
                "Download Questions",
                data=response,
                file_name=f"{role}_{experience_level}_interview_questions.md",
                mime="text/markdown",
            )
