# https://github.com/edwko/OuteTTS/blob/main/docs/interface_v2_usage.md
# https://www.soundboard.com/sb/Audrey_Hepburn_audio

import os
import outetts
from datetime import datetime

from speech_node import DownloadVoiceFiles, VOICE_SAMPLE_URLS, MP3Utils

DEVICE = "cuda"
OUTPUT_DIR = "output"
VOICE_PROFILE_PATH = f"{OUTPUT_DIR}/profile.json"
VOICE_DATA_DIR = "voice_data"
VOICE_SAMPLE_PATH = "voice_data/sense-sensibility_01_austen_64kb.mp3"
SAMPLE_START_TIME_IN_MILLI = 100_000
VOICE_SAMPLE_LENGTH_MILLI = 19_000  # 0-15_000 milliseconds
CLIPPED_SAMPLE_PATH = f"{OUTPUT_DIR}/voice_sample.wav"
SPEAKER_JSON_PATH = f"{OUTPUT_DIR}/profile.json"

os.makedirs(OUTPUT_DIR, exist_ok=True)

# Configure the model
model_config = outetts.HFModelConfig_v2(
    model_path="OuteAI/OuteTTS-0.3-1B",
    tokenizer_path="OuteAI/OuteTTS-0.3-1B",
    device=DEVICE,
)
# Initialize the interface
interface = outetts.InterfaceHF(model_version="0.3", cfg=model_config)

if not os.path.exists(VOICE_PROFILE_PATH):
    downloader = DownloadVoiceFiles(
        VOICE_SAMPLE_URLS,
        data_dir=VOICE_DATA_DIR,
    )
    MP3Utils.sample(
        VOICE_SAMPLE_PATH,
        length_milliseconds=VOICE_SAMPLE_LENGTH_MILLI,
        output_filepath=CLIPPED_SAMPLE_PATH,
        sample_start_time_in_milliseconds=SAMPLE_START_TIME_IN_MILLI,
    )
    speaker = interface.create_speaker(
        audio_path=CLIPPED_SAMPLE_PATH,
        whisper_model="large-v3.en",
        whisper_device=DEVICE,
    )
    interface.save_speaker(speaker, VOICE_PROFILE_PATH)
else:
    # You can create a speaker profile for voice cloning, which is compatible across all backends.
    speaker = interface.load_speaker(SPEAKER_JSON_PATH)


while True:

    text = input("What should I say? ")

    inference_start_time = datetime.now()
    # Generate speech
    gen_cfg = outetts.GenerationConfig(
        text=text,
        temperature=0.1,
        repetition_penalty=1.1,
        max_length=4096,
        speaker=speaker,
        voice_characteristics="worn out, ground down, exhausted, weary, tired, fatigued",
    )
    output = interface.generate(config=gen_cfg)
    print(f"Generation time: {datetime.now() - inference_start_time}")

    # Save the generated speech to a file
    print("Saving output to sample.wav")
    output.save("sample.wav")
    # output.play("sounddevice")
