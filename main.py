#Our main file
import speech_recognition as sr

# Cria um reconeceddor
r = sr.Recognizer()

# Abrir um microfone
with sr.Microphone() as source:
    while True:
        audio = r.listen(source) # Define o microfone como fonte de audio

        print(r.recognize_google(audio, language='pt'))