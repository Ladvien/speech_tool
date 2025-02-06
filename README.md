# speech-node
A text-to-speech server to inclusion in AI pipelines


## Links
- https://github.com/edwko/OuteTTS/blob/main/docs/interface_v2_usage.md
- https://github.com/edwko/OuteTTS
- https://huggingface.co/hexgrad/Kokoro-82M
- https://github.com/spotify/pedalboard/blob/master/examples/streaming_encode_mp3.py

### Python Audio Libraries
- https://github.com/librosa/librosa
- https://github.com/bastibe/python-soundfile

## Voices
- https://publicdomainreview.org/collection/orson-welles-show-1941/
- https://librivox.org/



## Dependencies

### Bark Specific
I had to onlly the patch linked here:
- https://github.com/suno-ai/bark/issues/626

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

### TTS Models
- https://huggingface.co/hexgrad/Kokoro-82M#releases

### Other Models
- [Recognizing Emotions in Speech](https://github.com/ddlBoJack/emotion2vec)
- [Speech Emotion Synthesis](https://github.com/NN-Project-2/Emotion-TTS-Emebddings)



### Upsampling
- https://github.com/ming024/FastSpeech2?tab=readme-ov-file
- https://rhasspy.github.io/piper-samples/