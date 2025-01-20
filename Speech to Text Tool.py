#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import speech_recognition as sr
from transformers import Wav2Vec2ForCTC, Wav2Vec2Processor
import torch
import librosa
import numpy as np

def transcribe_with_speechrecognition(audio_file):
    """
    Transcribe audio using the SpeechRecognition library.
    """
    recognizer = sr.Recognizer()
    try:
        with sr.AudioFile(audio_file) as source:
            audio_data = recognizer.record(source)
            text = recognizer.recognize_google(audio_data)
            return text
    except Exception as e:
        return f"Error with SpeechRecognition: {e}"

def transcribe_with_wav2vec(audio_file):
    """
    Transcribe audio using a pre-trained Wav2Vec 2.0 model.
    """
    try:
        # Load pre-trained model and processor
        model_name = "facebook/wav2vec2-base-960h"
        processor = Wav2Vec2Processor.from_pretrained(model_name)
        model = Wav2Vec2ForCTC.from_pretrained(model_name)

        # Load audio
        audio, rate = librosa.load(audio_file, sr=16000)  # Ensure 16kHz sampling rate
        input_values = processor(audio, return_tensors="pt", sampling_rate=rate).input_values

        # Perform transcription
        logits = model(input_values).logits
        predicted_ids = torch.argmax(logits, dim=-1)
        transcription = processor.decode(predicted_ids[0])

        return transcription
    except Exception as e:
        return f"Error with Wav2Vec: {e}"

if __name__ == "__main__":
    audio_path = r"C:\Users\Siya\OneDrive\Desktop\sample.wav"

    print("Transcription using SpeechRecognition:")
    sr_transcription = transcribe_with_speechrecognition(audio_path)
    print(sr_transcription)

    print("\nTranscription using Wav2Vec:")
    wav2vec_transcription = transcribe_with_wav2vec(audio_path)
    print(wav2vec_transcription)

