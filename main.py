import pyttsx3
import speech_recognition as sr
import datetime
import pyaudio
import webbrowser
import os
import pyjokes
from ecapture import ecapture as ec

engine = pyttsx3.init("sapi5")
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)
engine.setProperty("rate", 180)


def speak(audio):
    print("       ")
    print(f": {audio}")
    print("       ")
    engine.say(audio)
    engine.runAndWait()


def greetMe():
    hour = int(datetime.datetime.now().hour)
    if hour >= 0 and hour < 12:
        speak("Good Morning Mam !")

    elif hour >= 12 and hour < 18:
        speak("Good Afternoon Mam !")

    else:
        speak("Good Evening Mam !")

    # speak("I am Jarvis A I your virtual assistant")
    speak("Please tell me, How can I help you ?")


def takeCommand():
    r = sr.Recognizer()

    with sr.Microphone(device_index = 1) as source:

        print("Listening...")
        r.pause_threshold = 1
        r.energy_threshold = 100
        audio = r.listen(source,timeout = 5, phrase_time_limit = 5)  
        # audio = r.listen(source,0,4)  

    try:
        print("Recognizing...")
        query = r.recognize_google(audio, language='en-in')
        print(f"you said: {query}\n")

    except Exception as e:
        print(e)
        print("Unable to Recognize your voice.")
        return "None"

    return query

if __name__ == "__main__":
    clear = lambda: os.system('cls')

    # This function will clean any command before
    # execution of this python file
    clear()
    greetMe()

    while True:
        query = takeCommand().lower()

        if 'wikipedia' in query:
            speak('Searching Wikipedia...')

        elif 'open chrome' in query:
            codepath = r"C:\\Program Files\\Google\\Chrome\\Application\\Chrome"
            os.startfile(codepath)

        elif 'open google' in query:
            speak("Here you go to Google\n")
            webbrowser.open("google.com")

        elif 'open youtube' in query:
            speak("Here you go to Youtube\n")
            webbrowser.open("youtube.com")

        elif 'open spotify' in query:
            speak("Here you go to Spotify\n")
            webbrowser.open("spotify.com")

        elif 'open stackoverflow' in query:
            speak("Here you go to Stack Over Flow\n")
            webbrowser.open("stackoverflow.com")

        elif 'open github' in query:
            speak("Here you go to Github\n")
            webbrowser.open("github.com")

        elif "camera" in query or "take a photo" in query:
            ec.capture(0, "Jarvis Camera ", "img.jpg")

        # conversation
        elif "hello jarvis" in query:
            speak("Hello Mam, how are you ?")

        elif 'how are you' in query:
            speak("I am fine, Thank you")
            speak("How are you, Mam")

        elif 'I am fine' in query or 'good' in query:
            speak("It's good to know that you are fine")

        elif "thank you" in query:
            speak("you are welcome, Mam")

        elif "who i am" in query:
            speak("If you talk then definitely your human.")

        elif "why you came to world" in query:
            speak("Thanks to Darshika. further It's a secret")

        elif 'is love' in query:
            speak("It is 7th sense that destroy all other senses")

        elif "who are you" in query:
            speak("I am a virtual assistant created by Darshika")

        elif "who made you" in query or "who created you" in query:
            speak("I have been created by Darshika.")

        elif "what's your name" in query or "what is your name" in query:
            speak("My friends call me, Jarvis")
            
        elif "will you be my girlfriend" in query or "will you be my boyfriend" in query:
            speak("I'm not sure about, may be you should give me some time")

        elif "i love you" in query:
            speak("It's hard to understand")

        elif 'joke' in query:
            speak(pyjokes.get_joke())

        # elif "don't listen" in query or "stop listening" in query:
        #     speak("for how much time you want to stop Jarvis from listening")
        #     a = int(takeCommand())
        #     time.sleep(a)
        #     print(a)

        elif "wake up" in query:
            greetMe()

        elif "go to sleep" in query:
            speak("Ok Mam, you can call me anytime")
            break

        elif 'exit' in query:
            speak("Thanks for giving me your time")
            exit()

            