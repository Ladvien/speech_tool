from kokoro import KPipeline
import soundfile as sf


# Make sure lang_code matches voice
pipeline = KPipeline(
    lang_code="b",
    device="cpu",
    #  model="onnx-community/Kokoro-82M-ONNX",
)

while True:
    text = input("What should I say? ")

    generator = pipeline(
        text,
        voice="af_bella",  # <= change voice here
        speed=0.7,
        split_pattern=r"\n+",
    )
    for i, (gs, ps, audio) in enumerate(generator):
        print(i)  # i => index
        print(gs)  # gs => graphemes/text
        print(ps)  # ps => phonemes
        sf.write(f"{i}.wav", audio, 24000)  # save each audio file
