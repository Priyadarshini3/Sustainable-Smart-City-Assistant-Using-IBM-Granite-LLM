import requests
from core.config import settings

def ask_watson(question):
    url = f"https://us-south.ml.cloud.ibm.com/ml/v1/text/generation"

    headers = {
        "Authorization": f"Bearer {settings.WATSONX_API_KEY}",
        "Content-Type": "application/json"
    }

    data = {
        "model_id": settings.MODEL_ID,
        "input": question,
        "parameters": {
            "temperature": 0.7,
            "max_new_tokens": 200
        }
    }

    response = requests.post(url, headers=headers, json=data)

    if response.status_code == 200:
        return response.json().get("results", [{}])[0].get("generated_text", "No response")
    else:
        return f"Error: {response.status_code}, {response.text}"