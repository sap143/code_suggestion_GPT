import streamlit as st
from code_suggestion import analyze_and_suggest_improvements

def main():
    st.set_page_config(layout="wide")
    st.title("Code Improvement Suggestions")

    # Input text boxes for GitHub repository and file path in the sidebar
    with st.sidebar:
        repository = st.text_input("Enter GitHub Repository", "sap143/ecom_django")
        file_path = st.text_input("Enter File Path", "ecom/app/views.py")

    objectives = [
        "Enhance code quality and maintainability",
        "Improve code performance",
        "Strengthen testing and validation",
        "Identify and fix potential bugs",
    ]

    t1,t2,t3,t4 =st.tabs(objectives)

    with t1:

        if st.button(f"Analyze quality"):
            result = analyze_and_suggest_improvements(repository, file_path, "Enhance code quality and maintainability")
            st.subheader(f"Result for Enhance code quality and maintainability")
            st.markdown(result)

    with t2:

        if st.button(f"Analyze performance"):
            result = analyze_and_suggest_improvements(repository, file_path, "Improve code performance")
            st.subheader(f"Result for Improve code performance")
            st.markdown(result)

    with t3:

        if st.button(f"Analyze testing and validation"):
            result = analyze_and_suggest_improvements(repository, file_path, "Strengthen testing and validation")
            st.subheader(f"Result for Strengthen testing and validation")
            st.markdown(result)


    with t4:

        if st.button(f"Analyze fix potential bugs"):
            result = analyze_and_suggest_improvements(repository, file_path, "Identify and fix potential bugs")
            st.subheader(f"Result for Identify and fix potential bugs")
            st.markdown(result)

if __name__ == "__main__":
    main()


