import io
from kokoro import KPipeline
import soundfile as sf
from typing import Union
from fastapi import FastAPI

# from fastapi.responses import FileResponse
from fastapi.responses import StreamingResponse
from uuid import uuid4

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

    def iterfile():
        buffer = io.BytesIO()
        for _, _, audio in generator:
            sf.write(
                buffer,
                audio,
                samplerate=24000,
                format="WAV",
            )
            buffer.seek(0)
            yield buffer.read()
            buffer.truncate(0)

    return StreamingResponse(iterfile(), media_type="audio/wav")
