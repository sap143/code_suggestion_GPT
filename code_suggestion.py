import base64
import os
import requests
from openai import OpenAI
from dotenv import load_dotenv, find_dotenv

# Set your OpenAI API key and GitHub Personal Access Token as environment variables
_ = load_dotenv(find_dotenv())
OPENAI_API_KEY = os.environ['OPENAI_API_KEY']
GITHUB_API_KEY = os.environ['GITHUB_API_KEY']
client = OpenAI(api_key=OPENAI_API_KEY)




def get_file_contents(repo, file_path):
    url = f"https://api.github.com/repos/{repo}/contents/{file_path}"
    headers = {"Authorization": f"Bearer {GITHUB_API_KEY}"}
    
    response = requests.get(url, headers=headers)
    response.raise_for_status()  

    content = response.json().get("content", "")
    decoded_content = base64.b64decode(content).decode("utf-8")
    return decoded_content

def analyze_code_with_chatgpt(code, objective):
    prompt = f"{objective}:\n\n{code}\n\nSuggestions:"
    messages=[
                {"role": "system", "content": "You are a helpful code assistant."},
                {"role": "user", "content": prompt},
            ]
    
    response = client.chat.completions.create(
    messages=messages,
    model="gpt-3.5-turbo",  
    max_tokens=1048,
    n=1,
    stop=None)
    
    suggestions = response.choices[0].message.content 
    return suggestions

def analyze_and_suggest_improvements(repo, file_path, objective):
    try:
        code = get_file_contents(repo, file_path)
        
        if not code:
            print(f"Error: Unable to retrieve code from {file_path}")
            return

        suggestions = analyze_code_with_chatgpt(code, objective)
        return suggestions
    except requests.exceptions.RequestException as e:
        print(f"GitHub API Error: {str(e)}")
    except Exception as e:
        print(f"Unexpected Error: {str(e)}")

if __name__ == "__main__":
    # Replace with your GitHub repository and file path
    repository = "sap143/ecom_django"
    file_path = "ecom/app/views.py"

    objectives = [
        "Enhance code quality and maintainability",
        "Improve code performance",
        "Strengthen testing and validation",
        "Identify and fix potential bugs",
    ]

    for objective in objectives:
        analyze_and_suggest_improvements(repository, file_path, objective)
