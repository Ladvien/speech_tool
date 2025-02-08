import os
import yaml
from fastapi import FastAPI
from speech_node import SpeechNodeServer, Config


CONFIG_PATH = "config.yaml"

config = Config(**yaml.safe_load(open(CONFIG_PATH, "r")))

app = FastAPI()
speech_node = SpeechNodeServer(config.node)
app.include_router(speech_node.router)
