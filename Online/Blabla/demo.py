import speech_recognition as sr

# Load the audio file
audio_file = sr.AudioFile("demo.wmv")

# Create a recognition object
recognizer = sr.Recognizer()

# Read the audio file
with audio_file as source:
    audio = recognizer.record(source)

# Recognize the speech in the audio file
text = recognizer.recognize_google(audio)

print(text)