import io
from kokoro import KPipeline
import soundfile as sf
from typing import Union
from fastapi import FastAPI, APIRouter
import yaml
from fastapi.responses import StreamingResponse
from uuid import uuid4
import os

from speech_node.config import Config

CONFIG_PATH = os.environ.get("NODE_CONFIG_PATH", "config.yaml")

with open(CONFIG_PATH, "r") as file:
    config = Config(**yaml.safe_load(file))


class SpeechNodeServer:

    def __init__(self, config: Config):
        self.config = config
        self.router = APIRouter()

        self.pipeline = KPipeline(
            lang_code="b",
            device="cpu",
            #  model="onnx-community/Kokoro-82M-ONNX",
        )

        self.router.add_api_route(
            "/node/speech",
            self.generate_speech,
            methods=["GET"],
        )

    def generate_speech(
        self,
        text: str,
        voice: str,
        speed: Union[float, int],
        split_pattern: str,
    ):

        unique_id = str(uuid4())

        generator = self.pipeline(
            text,
            voice=voice,  # <= change voice he re
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
