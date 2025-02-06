import requests

HOST = 'http://localhost:8000'

# Get the wave file from the server
url = f"{HOST}/node/speech"
response = requests.get(url, params={
    "text": "What's up baby?",
    "voice": "af_bella",
    "speed": 0.7,
    "split_pattern": r"\n+",
})

print(response.status_code)

with open('retrieved_audi.wav', 'wb') as f:
    f.write(response.content)