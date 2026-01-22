#!/usr/bin/env python
# coding: utf-8

# In[ ]:

import speech_recognition as sr
from pydub import AudioSegment
import os
import time


def convert_mp3_to_wav(mp3_path):
    """
    Convert MP3 audio file to WAV (16kHz, mono) for speech recognition.
    """
    audio = AudioSegment.from_mp3(mp3_path)
    audio = audio.set_channels(1).set_frame_rate(16000)

    wav_path = mp3_path.replace(".mp3", ".wav")
    audio.export(wav_path, format="wav")

    return wav_path


def speech_to_text(audio_path, language="en-US"):
    """
    Convert speech audio file to text.
    Supports WAV and MP3 formats.
    """

    recognizer = sr.Recognizer()

    # Convert MP3 to WAV if needed
    if audio_path.lower().endswith(".mp3"):
        print("Converting MP3 to WAV for better accuracy...")
        audio_path = convert_mp3_to_wav(audio_path)

    try:
        with sr.AudioFile(audio_path) as source:
            audio = recognizer.record(source)

        start_time = time.time()
        text = recognizer.recognize_google(audio, language=language)
        end_time = time.time()

        print(f"Recognition Time: {round(end_time - start_time, 2)} seconds")
        return text

    except sr.UnknownValueError:
        return "Speech could not be understood."

    except sr.RequestError:
        return "Speech recognition service unavailable."

    except Exception as e:
        return f"Error: {str(e)}"



audio_file = input("Enter path to audio file (MP3 or WAV): ")

if not os.path.exists(audio_file):
    print("Audio file not found.")
else:
    result = speech_to_text(audio_file)
    print("\nRecognized Text:\n")
    print(result)



