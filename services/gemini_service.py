import requests
import os
from dotenv import load_dotenv

load_dotenv()

API_KEY = os.getenv("OPENROUTER_API_KEY")


def analyze_bug(code):

    prompt = f"""
    You are an expert Python bug fixing AI.

    Analyze the given code.

    Give response in this format:

    Bug:
    Explanation:
    Fixed Code:

    Code:
    {code}
    """

    headers = {
        "Authorization": f"Bearer {API_KEY}",
        "Content-Type": "application/json",
        "HTTP-Referer": "http://localhost:5000",
        "X-Title": "Bug Fix Agent"
    }

    data = {
        "model": "openai/gpt-3.5-turbo",
        "messages": [
            {
                "role": "user",
                "content": prompt
            }
        ]
    }

    try:

        response = requests.post(
            "https://openrouter.ai/api/v1/chat/completions",
            headers=headers,
            json=data
        )

        result = response.json()

        print(result)

        if "choices" in result:

            return result["choices"][0]["message"]["content"]

        else:

            return f"API Error: {result}"

    except Exception as e:

        return f"Error: {str(e)}"