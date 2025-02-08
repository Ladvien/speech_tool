import io
# from kokoro import KPipeline
from kokoro_onnx import Kokoro
import soundfile as sf
from typing import Union
from fastapi import FastAPI, APIRouter
import yaml
from fastapi.responses import StreamingResponse
from uuid import uuid4
import os

from speech_node.config import NodeConfig


class SpeechNodeServer:

    def __init__(self, config: NodeConfig):
        self.config = config
        self.router = APIRouter()

        # self.pipeline = KPipeline(
        #     lang_code=self.config.pipeline.language_code,
        #     device=self.config.pipeline.device,
        #     trf=self.config.pipeline.use_transformer,
        #     #  model="onnx-community/Kokoro-82M-ONNX",
        # )

        self.model = Kokoro("kokoro-v1.0.onnx", "voices-v1.0.bin")

        self.router.add_api_route(
            "/node/speech",
            self.generate_speech,
            methods=["GET"],
        )

    def generate_speech(
        self,
        text: str,
        voice: str = None,
        speed: Union[float, int] = None,
        split_pattern: str = None,
    ):

        unique_id = str(uuid4())

        if voice:
            self.config.pipeline.voice = voice
        if speed:
            self.config.pipeline.speed = speed
        if split_pattern:
            self.config.pipeline.split_pattern = split_pattern


        stream = self.model.create_stream(
            text,
            voice=self.config.pipeline.voice,
            speed=self.config.pipeline.speed,
            lang=self.config.pipeline.language_code,
        )

        # generator = self.pipeline(
        #     text,
        #     voice=voice,
        #     speed=speed,
        #     split_pattern=split_pattern,
        # )

        async def iterfile():
            buffer = io.BytesIO()
            async for sample, sample_rate in stream:
                sf.write(
                    buffer,
                    sample,
                    samplerate=sample_rate,
                    format=self.config.response.format,
                    compression_level=self.config.response.compression_level,
                )
                buffer.seek(0)
                yield buffer.read()
                buffer.truncate(0)

        return StreamingResponse(
            iterfile(),
            media_type="audio/wav",
        )
