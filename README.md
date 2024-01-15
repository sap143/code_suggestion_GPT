# Code Improvement Suggestions

This Streamlit application analyzes code using OpenAI's GPT-3.5 Turbo model and suggests improvements in terms of code quality, performance, testing, and bug fixes.

## Prerequisites

- Python 3.6 or later
- GitHub account with a Personal Access Token
- OpenAI API key

## Setup

1. Clone the repository:

    ```bash
    git clone https://github.com/yourusername/your-repo.git
    cd your-repo
    ```

2. Install dependencies:

    ```bash
    pip install -r requirements.txt
    ```

3. Set up environment variables:

    Create a `.env` file in the project root and add the following:

    ```env
    OPENAI_API_KEY=your_openai_api_key
    GITHUB_API_KEY=your_github_personal_access_token
    ```

    Replace `your_openai_api_key` and `your_github_personal_access_token` with your actual OpenAI API key and GitHub Personal Access Token.

## Running the Application

```bash
streamlit run app.py
