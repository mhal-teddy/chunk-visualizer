import json
import requests

def jina_ai_chunking(text: str) -> list[str]:
    url = "https://tokenize.jina.ai/"
    headers = {
        "Content-Type": "application/json",
    }
    data = {
        "content": text,
        "return_chunks": "true"
    }

    response = requests.post(url, headers=headers, json=data)

    return json.loads(response.text)["chunks"]
