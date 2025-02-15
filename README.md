# speech_neuron
A text-to-speech server to inclusion in AI pipelines


## Quick Start
Run:
```sh
pip install speech_neuron
```

Create a `config.yaml` file with the following content:
# TODO: Add config.yaml example

Create a `main.py` file with the following content:
```py
import os
import yaml
from fastapi import FastAPI
import uvicorn
from speech_neuron import SpeechNeuronServer, NodeConfig

CONFIG_PATH = os.environ.get("NODE_CONFIG_PATH", "config.yaml")
config = NodeConfig(**yaml.safe_load(open(CONFIG_PATH, "r")))

app = FastAPI()

speech_neuron = SpeechNeuronServer(config)
app.include_router(speech_neuron.router)

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)
```

Run:
```sh
python main.py
```

## Dependencies

### Linux


#### Ubuntu
```sh
sudo apt update
sudo apt install libglslang-dev
```

#### Manjaro
```sh
sudo pacman -S ffmpeg glslang

# Check for version mismatch
find /usr -name "libglslang-default-resource-limits.so*"
# If version mismatch
sudo ln -s /usr/lib/libglslang-default-resource-limits.so.15 /usr/lib/libglslang-default-resource-limits.so.14

# Check for version mismatch
find /usr -name "libSPIRV.so*"
# If version mismatch

sudo ldconfig
```

If NVIDIA is not working:
```sh
sudo modprobe -r nvidia_uvm
sudo modprobe nvidia_uvm
```

### MacOS
```
brew install ffmpeg
brew install glslang
```