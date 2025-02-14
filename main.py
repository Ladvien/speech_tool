import os
import yaml
from fastapi import FastAPI
from speech_neuron import SpeechNeuronServer, NodeConfig

CONFIG_PATH = os.environ.get("NODE_CONFIG_PATH", "config.yaml")
config = NodeConfig(**yaml.safe_load(open(CONFIG_PATH, "r")))

app = FastAPI()

speech_neuron = SpeechNeuronServer(config)
app.include_router(speech_neuron.router)
