from ast import main
from datetime import datetime
import webbrowser
import pyaudio
import wikipedia
import speech_recognition as sr
import pyttsx3
import os

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')

engine.setProperty('voice',voices[0].id)
def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def wishMe():
    hour = int(datetime.now().hour)
    if hour >= 0 and hour<12:
        speak('Good Morning Vamsidhar')
    elif hour>=12 and hour<=16:
        speak('Good Afternoon Vamsidhar')
    else:
        speak('Good Evening Vamsidhar')

    speak("I am Ushvathama, your personal desktop assistant. Please let me know how can I help you.")

def takeCommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        r.energy_threshold = 300
        audio = r.listen(source)
    
    try:
        print("Recognising.....")
        query = r.recognize_google(audio, language='en-in')
        print(f'User said: {query}\n')

    except Exception as e:
        # print(0)
        print('Say that again please....')
        return "None"
    return query
if __name__ == "__main__":
    wishMe()
    while(True):

        query = takeCommand().lower()
    #Logic to executing tasks based on query
        if 'wikipedia' in query:
            speak("Searching wikipedia.....")
            query = query.replace("wikipedia","")
            results = wikipedia.summary(query,sentences = 2)
            speak("According to Wikipedia")
            print(results)
            speak(results)
    
        elif 'open youtube' in query:
            speak('Opening Youtube')
            webbrowser.open('youtube.com')
            continue
    
        elif 'open brave' in query:
            speak('Opening Brave')
            webbrowser.open('brave.com')
            continue
        
        elif 'open brave' in query:
            speak('Opening Brave')
            webbrowser.open('brave.com')
            continue

        elif 'open stack overflow' in query:
            speak('Opening Stack Overflow')
            webbrowser.open('stackoverflow.com')
            continue

        elif 'bye' in query:
            speak('Okay! See you later.')
            exit()
