import re
import requests

# === CONFIGURATION ===
OPENROUTER_API_KEY = "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"
OPENROUTER_URL = "https://openrouter.ai/api/v1/chat/completions"
MODEL_NAME = "deepseek/deepseek-chat-v3-0324:free"

def clean_response(text):
    # Smart formatting, preserve paragraphs
    text = re.sub(r'[\\*#`>{}\[\]_|\-]', '', text)
    return text.strip()

def ask_nova(prompt):
    headers = {
        "Authorization": f"Bearer {OPENROUTER_API_KEY}",
        "Content-Type": "application/json"
    }

    data = {
        "model": MODEL_NAME,
        "messages": [
            {"role": "system", "content": "You are NOVA-X, a helpful assistant."},
            {"role": "user", "content": prompt}
        ]
    }

    try:
        response = requests.post(OPENROUTER_URL, headers=headers, json=data, timeout=10)
        if response.status_code == 200:
            raw_text = response.json()["choices"][0]["message"]["content"]
            return clean_response(raw_text)
        else:
            return f"Error {response.status_code}: {response.text}"
    except Exception as e:
        return f"Connection Error: {e}"
