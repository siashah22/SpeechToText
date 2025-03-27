#!/usr/bin/env python
# coding: utf-8

# In[ ]:

#Converting .mp3 audio file to .wav file 
import os
import subprocess

mp3_file = r"C:\Users\Public\S2T\speech sample.mp3"
wav_file = r"C:\Users\Public\S2T\speech sample.wav"
ffmpeg_path = r"C:\Users\Siya\ffmpeg-2025-03-24-git-cbbc927a67-full_build\ffmpeg-2025-03-24-git-cbbc927a67-full_build\bin\ffmpeg.exe" # Change this to your actual FFmpeg path
subprocess.run([ffmpeg_path, "-i", mp3_file, "-ar", "16000", "-ac", "1", "-c:a", "pcm_s16le", wav_file], shell=True)


if os.path.exists(wav_file):
    print(f"✅ WAV file created successfully: {wav_file}")
else:
    print("❌ WAV file creation failed!")

#Loading the Vosk Model 
import os
from vosk import Model

model_dir = r"C:\Users\Public\S2T\models\vosk-model-en-us-0.22\vosk-model-en-us-0.22"

# Check if model directory exists
if not os.path.exists(model_dir):
    raise Exception("❌ Model directory not found! Check the path.")

# Try to load the model
try:
    model = Model(model_dir)
    print("✅ Vosk model loaded successfully!")
except Exception as e:
    print("❌ Error loading Vosk model:", e)


#Transcribing the speech to text 
import os
import subprocess
import wave
import json
from vosk import Model, KaldiRecognizer


# Set paths to files
mp3_file = r"C:\Users\Public\S2T\speech sample.mp3"  # Ensure the MP3 file is in the same directory as this script
wav_file = r"C:\Users\Public\S2T\speech sample.wav"
model_dir = r"C:\Users\Public\S2T\models\vosk-model-en-us-0.22\vosk-model-en-us-0.22" # Ensure the Vosk model is in "models/" folder

def transcribe_audio(wav_path, model_dir):
    """Transcribe WAV audio using Vosk (Offline)."""
    model = Model(model_dir)
    recognizer = KaldiRecognizer(model, 16000)

    with wave.open(wav_path, "rb") as wf:
        while True:
            data = wf.readframes(4000)
            if len(data) == 0:
                break
            recognizer.AcceptWaveform(data)

        result = json.loads(recognizer.FinalResult())
        return result["text"]

# Transcribe audio offline
transcription = transcribe_audio(wav_file, model_dir)
print("Transcription:", transcription)


