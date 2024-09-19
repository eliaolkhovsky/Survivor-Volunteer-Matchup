import pyttsx3


def txt_to_speech(word):
    engine = pyttsx3.init()
    engine.say(word)
    engine.runAndWait()
