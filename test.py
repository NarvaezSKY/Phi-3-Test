import requests

url = 'http://localhost:8000/generate'
payload = {
    'prompt': 'What is the capital of France?'
}

try:
    response = requests.post(url, json=payload)
    response.raise_for_status()
    data = response.json()
    print('Response from model:')
    print(data['response'])
except requests.exceptions.RequestException as e:
    print('Error:', e)
