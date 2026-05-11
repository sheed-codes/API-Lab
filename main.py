# This program demonstrates how to use an API in Python
# It makes multiple requests to the OpenAI API and prints responses

import os
import requests
from dotenv import load_dotenv

# Load API key from .env file
load_dotenv()
API_KEY = os.getenv("OPENAI_API_KEY")

# OpenAI endpoint
URL = "https://api.openai.com/v1/chat/completions"

# Headers
headers = {
    "Authorization": f"Bearer {API_KEY}",
    "Content-Type": "application/json"
}

# Function to send a prompt to the API
def ask_chatbot(prompt):
    data = {
        "model": "gpt-4o-mini",
        "messages": [
            {"role": "user", "content": prompt}
        ]
    }

    response = requests.post(URL, headers=headers, json=data)

    # Error handling
    if response.status_code != 200:
        print("Error:", response.status_code)
        print(response.text)
        return None

    result = response.json()
    return result["choices"][0]["message"]["content"]


# ====== 3 REQUIRED API CALLS ======

prompts = [
    "Explain what an API is in simple terms.",
    "Tell a short joke about programming.",
    "Why is artificial intelligence important today?"
]

print("\nAPI Lab - OpenAI Example\n")

for i, prompt in enumerate(prompts):
    print(f"Test Case {i+1}")
    print(f"Prompt: {prompt}")

    answer = ask_chatbot(prompt)

    if answer:
        print("Response:")
        print(answer)
    else:
        print("Failed to get response.")

    print("\n-----------------------------\n")