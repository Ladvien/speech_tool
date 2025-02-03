import outetts

# Configure the model
model_config = outetts.HFModelConfig_v1(
    model_path="OuteAI/OuteTTS-0.2-500M",
    language="en",  # Supported languages in v0.2: en, zh, ja, ko
)

# Initialize the interface
interface = outetts.InterfaceHF(model_version="0.2", cfg=model_config)

speaker = interface.load_default_speaker(name="female_1")

# Print available default speakers
interface.print_default_speakers()

# Load a default speaker


# Generate speech
output = interface.generate(
    text="Listen here mother fucker, I don't care what you want to do, knock it off.",
    temperature=0.1,
    repetition_penalty=1.1,
    max_length=4096,
    # Optional: Use a speaker profile for consistent voice characteristics
    # Without a speaker profile, the model will generate a voice with random characteristics
    speaker=speaker,
)

# Save the generated speech to a file
output.save("output.wav")

# Optional: Play the generated audio
# output.play()


# import torch
# import warnings
# import numpy as np
# import sounddevice as sd
# from transformers import AutoProcessor, BarkModel

# # Ignore non-critical warnings
# warnings.simplefilter("ignore", UserWarning)

# # Choose device (CPU or Apple MPS)
# # device = "mps" if torch.backends.mps.is_available() else "cpu"
# device = "cpu"

# # Load model and processor
# model = BarkModel.from_pretrained("suno/bark").to(device)
# processor = AutoProcessor.from_pretrained("suno/bark")


# model.config.pad_token_id = model.config.eos_token_id  # Avoids warning


# # Input text
# text = "Try it mother fucker"

# # Process input text
# inputs = processor(text, return_tensors="pt").to(device)


# inputs["attention_mask"] = torch.ones_like(inputs["input_ids"], dtype=torch.long)

# # Generate speech (returns a tensor)
# output = model.generate(**inputs)

# # Extract audio tensor
# audio_tensor = output.squeeze().cpu()

# # Convert to NumPy array
# audio_numpy = audio_tensor.numpy()

# # Set sample rate (Bark typically uses 24kHz)
# sample_rate = 24000  # Adjust if needed

# # Play audio using sounddevice
# sd.play(audio_numpy, samplerate=sample_rate)
# sd.wait()  # Wait until playback finishes
