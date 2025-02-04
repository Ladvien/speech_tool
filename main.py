# https://github.com/edwko/OuteTTS/blob/main/docs/interface_v2_usage.md
# https://www.soundboard.com/sb/Audrey_Hepburn_audio

import os
import outetts

from speech_node import DownloadVoiceFiles, VOICE_SAMPLE_URLS, MP3Utils

OUTPUT_DIR = "output"


VOICE_PROFILE_PATH = f"{OUTPUT_DIR}/profile.json"
VOICE_DATA_DIR = "voice_data"
VOICE_SAMPLE_PATH = "voice_data/sense-sensibility_01_austen_64kb.mp3"
VOICE_SAMPLE_LENGTH_MILLI = 20_000  # 0-30_000 milliseconds
CLIPPED_SAMPLE_PATH = f"{OUTPUT_DIR}/voice_sample.mp3"

os.makedirs(OUTPUT_DIR, exist_ok=True)

# Configure the model
model_config = outetts.HFModelConfig_v2(
    model_path="OuteAI/OuteTTS-0.3-1B",
    tokenizer_path="OuteAI/OuteTTS-0.3-1B",
)
# Initialize the interface
interface = outetts.InterfaceHF(model_version="0.3", cfg=model_config)

if not os.path.exists(VOICE_PROFILE_PATH):
    downloader = DownloadVoiceFiles(
        VOICE_SAMPLE_URLS,
        data_dir=VOICE_DATA_DIR,
    )
    MP3Utils.clip(
        VOICE_SAMPLE_PATH,
        length_milliseconds=VOICE_SAMPLE_LENGTH_MILLI,
        output_filepath=CLIPPED_SAMPLE_PATH,
    )
    speaker = interface.create_speaker(
        audio_path=CLIPPED_SAMPLE_PATH,
        whisper_model="large-v3",
        whisper_device="cpu",
    )
    interface.save_speaker(speaker, VOICE_PROFILE_PATH)
else:
    # You can create a speaker profile for voice cloning, which is compatible across all backends.
    speaker = interface.load_speaker(CLIPPED_SAMPLE_PATH)


# Generate speech
gen_cfg = outetts.GenerationConfig(
    text="Listen here, jerk! I know you think your are funny. But that's simply not the case!",
    temperature=0.4,
    repetition_penalty=1.1,
    max_length=4096,
    speaker=speaker,
)
output = interface.generate(config=gen_cfg)

# Save the generated speech to a file
output.save("sample.wav")
