import pyttsx3  # converts text to speech
import speech_recognition as sr

engine = pyttsx3.init()  # Initilaize text-to-speech engine

def speak(audio):  # function for assistant to speak
    engine.say(audio)
    engine.runAndWait()  # without this command, the assistant won't be audible to us

def takecommand():  # function to take an audio input from the user
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print('Listening...')
        r.pause_threshold = 2
        r.adjust_for_ambient_noise(
            source
        )  # listen for 1 second to calibrate the energy threshold for ambient noise levels
        audio = r.listen(source)
        try:                                            # error handling
            print('Recognizing...')
            # using google for voice recognition
            query = r.recognize_google(audio, language='en-in')
            print(f'User said: {query}\n')

        except Exception as e:
            # 'say that again' will be printed in case of improper voice
            print('Say that again please...')
            return 'None'
    return query