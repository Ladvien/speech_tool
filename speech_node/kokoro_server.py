from kokoro import KPipeline
import soundfile as sf
from typing import Union
from fastapi import FastAPI
from fastapi.responses import FileResponse
from uuid import uuid4

# class KokoroServer:

#     def __init__(self):
app = FastAPI()

@app.get(
    path="/node/speech",
)
async def generate_speech(
    text: str,
    voice: str,
    speed: Union[float, int],
    split_pattern: str,
):
    
    unique_id = str(uuid4())

    pipeline = KPipeline(
        lang_code="b",
        device="cpu",
        #  model="onnx-community/Kokoro-82M-ONNX",
    )
    generator = pipeline(
        text,
        voice=voice,  # <= change voice here
        speed=speed,
        split_pattern=split_pattern,
    )
    for i, (gs, ps, audio) in enumerate(generator):
        filename = f"{unique_id}_{i}.wav"
        sf.write(filename, audio, 24000)

    return FileResponse(filename, media_type="audio/mpeg")

