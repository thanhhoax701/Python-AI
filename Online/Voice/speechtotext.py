# import speech_recognition as sr
# import threading
# import time
# from queue import Queue

# listen_recognizer = sr.Recognizer()
# process_recognizer = sr.Recognizer()

# audios_to_process = Queue()

# def callback(recognizer, audio_data):
#     if audio_data:
#         audios_to_process.put(audio_data)

# def listen():
#     source = sr.Microphone()
#     stop_listening = listen_recognizer.listen_in_background(source, callback, 1)
#     return stop_listening

# def process_thread_func():
#     while True:
#         if audios_to_process.empty():
#             time.sleep(2)
#             continue
#         audio = audios_to_process.get()
#         if audio:
#             try:
#                 text = process_recognizer.recognize_google(audio)
#             except:
#                 pass
#             else:
#                 print(text)

# stop_listening = listen()
# process_thread = threading.Thread(target=process_thread_func)
# process_thread.start()

# input()

# stop_listening()


# import speech_recognition as sr
# r = sr.Recognizer()
# with sr.Microphone() as source:
#     audio_data = r.record(source, duration=5)
#     print("Recognizering...")
#     try:
#         text = r.recognize_google(audio_data, language=vi)
#     except:
#         text=""
#     print(text)


