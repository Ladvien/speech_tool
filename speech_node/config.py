from dataclasses import dataclass
from typing import Optional


@dataclass
class ResponseConfig:
    type: str = "file"  # file or stream
    sample_rate: int = 24000  # 16000, 24000, 44100, 48000
    format: str = "wav"  # wav, flac, ogg, mp3
    compression_level: int = 0  # 0-9

    def __post_init__(self):
        self.type = self.type or "file"


@dataclass
class PipelineConfig:
    model: Optional[str]
    device: str = "cpu"  # cpu, cuda, or maybe mps
    use_transformer: bool = False  # True or False
    language_code: str = "b"  # a, b, c, d, e, f, g, h, i, j, k, l, m, n, o, p
    speed: float = 1.0
    voice: str = "af_bella"
    split_pattern: str = r"\n+"

    def __post_init__(self):
        self.model = self.model or "onnx-community/Kokoro-82M-ONNX"


@dataclass
class NodeConfig:
    name: str = "speech"
    response: ResponseConfig = None
    pipeline: PipelineConfig = None

    def __post_init__(self):
        self.response = ResponseConfig(**self.response)
        self.pipeline = PipelineConfig(**self.pipeline)


@dataclass
class Config:
    node: NodeConfig

    def __post_init__(self):
        self.node = NodeConfig(**self.node)
