import os
import yaml
from fastapi import FastAPI
import uvicorn
from speech_tool import SpeechToolServer, NodeConfig

CONFIG_PATH = os.environ.get("NODE_CONFIG_PATH", "config.yaml")
config = NodeConfig(**yaml.safe_load(open(CONFIG_PATH, "r")))

app = FastAPI()

speech_tool = SpeechToolServer(config)
app.include_router(speech_tool.router)

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)
