import os
import requests

api_key = os.getenv("OPENROUTER_API_KEY")

if not api_key:
    raise ValueError("Defina OPENROUTER_API_KEY no ambiente.")

url = "https://openrouter.ai/api/v1/chat/completions"
headers = {
    "Authorization": f"Bearer {api_key}",
    "Content-Type": "application/json",
}
payload = {
    "model": "openai/gpt-4o-mini",
    "messages": [{"role": "user", "content": "Diga olá do OpenRouter!"}],
}

resp = requests.post(url, headers=headers, json=payload, timeout=60)
resp.raise_for_status()
print(resp.json()["choices"][0]["message"]["content"])
