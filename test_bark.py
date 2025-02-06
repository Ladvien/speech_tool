from bark import SAMPLE_RATE, generate_audio, preload_models
from scipy.io.wavfile import write as write_wav
from datetime import datetime

# download and load all models
preload_models()

# # generate audio from text
# text_prompt = """
#      Hello, my name is Suno. And, uh — and I like pizza. [laughs]
#      But I also have other interests such as playing tic tac toe.
# """

while True:
    inference_start_time = datetime.now()
    text_prompt = input("Enter text prompt: ")
    audio_array = generate_audio(text_prompt)
    inference_end_time = datetime.now()
    print(f"Audio generated in {inference_end_time - inference_start_time}")

    # save audio to disk
    write_wav("bark_generation.wav", SAMPLE_RATE, audio_array)
