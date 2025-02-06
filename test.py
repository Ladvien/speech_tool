# 3️⃣ Initalize a pipeline
from kokoro import KPipeline
import soundfile as sf


pipeline = KPipeline(lang_code="b", model=,)  # <= make sure lang_code matches voice

# 4️⃣ Generate, display, and save audio files in a loop.
while True:
    text = input("What should I say? ")
    generator = pipeline(
        text, voice="af_bella", speed=0.7, split_pattern=r"\n+"  # <= change voice here
    )
    for i, (gs, ps, audio) in enumerate(generator):
        print(i)  # i => index
        print(gs)  # gs => graphemes/text
        print(ps)  # ps => phonemes
        sf.write(f"{i}.wav", audio, 24000)  # save each audio file
