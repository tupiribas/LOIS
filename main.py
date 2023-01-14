import speech_recognition as sr

r = sr.Recognizer()

# Abrir o microfone e capturar a voz
with sr.Microphone() as fala:
    while True:
        try:
            print('Microfone ligado! \nDiga alguma coisa, amigo!')
            # Grava a fala
            audio = r.listen(fala)
            # Traduz o que foi gravado e mostra em tempo real
            print('Você disse: ', r.recognize_google(audio, language='pt'))
        except sr.UnknownValueError:
            pass
        except sr.RequestError:
            pass
