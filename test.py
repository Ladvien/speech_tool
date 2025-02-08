"""
Note: on Linux you need to run this as well: apt-get install portaudio19-dev

pip install kokoro-onnx sounddevice

wget https://github.com/thewh1teagle/kokoro-onnx/releases/download/model-files-v1.0/kokoro-v1.0.onnx

python examples/play.py
"""

from datetime import datetime
import sounddevice as sd
import soundfile as sf
from kokoro_onnx import Kokoro

kokoro = Kokoro("kokoro-v1.0.onnx", "voices-v1.0.bin")


while True:
    text = input("Enter text: ")
    start_time = datetime.now()
    samples, sample_rate = kokoro.create(
        text, voice="af_sarah", speed=1.0, lang="en-us",
    )
    print("Playing audio...")
    end_time = datetime.now()
    print("Time taken: ", end_time - start_time)

    sf.write("output.wav", samples, sample_rate)