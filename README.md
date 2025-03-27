# SpeechToText

# DESCRIPTION OF SPEECH TO TEXT TOOL 


This program converts speech from an **MP3 file** to **text** using **Vosk**, an offline speech recognition library. The process is divided into two main steps:  
1. **Audio Conversion** – Converts an **MP3 file** into a **WAV format** (16 kHz, mono) using **FFmpeg**.  
2. **Speech Recognition** – Uses the **Vosk speech recognition model** to transcribe the WAV file into text without requiring an internet connection.  

## ** How It Works**  

### **Step 1: Convert MP3 to WAV**  
- **How?** The program runs an **FFmpeg command** to convert the MP3 file into the correct format.  

### **Step 2: Perform Speech Recognition**  
- The **Vosk model** is loaded from the specified path.  
- The **KaldiRecognizer** processes the WAV file in small chunks to handle large files efficiently.  
- The recognized text is extracted from the final result and displayed.  

## **📌 Features**  
✔ **Works offline** – No internet required for transcription.  
✔ **High accuracy** – Uses Vosk’s optimized AI models.  
✔ **Supports multiple languages** – Different language models can be used.  
✔ **Lightweight** – Runs efficiently even on low-end devices.  

Would you like additional details, such as **real-time speech recognition** from a microphone? 🎙️
