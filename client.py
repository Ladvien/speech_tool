import requests
import io
import sounddevice as sd
import soundfile as sf
from datetime import datetime

HOST = "http://0.0.0.0:8000"
# HOST = "http://192.168.1.137:8000"
url = f"{HOST}/node/speech"

start = datetime.now()
response = requests.get(
    url,
    params={
        "text": """Anyway, it was the Saturday of the football game with Saxon Hall. 
                   The game with Saxon Hall was supposed to be a very big deal around Pencey. 
        """,
        "voice": "af_bella",
        "speed": 1.1,
        "split_pattern": r"\n+",
    },
    stream=True,
)


# Read the streamed response into memory
audio_buffer = io.BytesIO()
for chunk in response.iter_content(chunk_size=4096):
    if chunk:
        audio_buffer.write(chunk)

# Play the audio in real-time
audio_buffer.seek(0)  # Reset buffer for reading
data, samplerate = sf.read(audio_buffer)
sd.play(data, samplerate)
sd.wait()  # Wait for audio to finish playing

print(f"Time taken: {datetime.now() - start}")
