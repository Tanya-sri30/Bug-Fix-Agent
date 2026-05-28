import requests
import os
from dotenv import load_dotenv

load_dotenv()

API_KEY = os.getenv("OPENROUTER_API_KEY")


def analyze_bug(code, language):

    prompt =  f"""
    You are an expert {language} debugging AI.

    Analyze the code carefully.

    Return:
    1. Error Type
    2. Root Cause
    3. Explanation
    4. Fixed Code

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