from ast import main
from datetime import datetime
import webbrowser
import pyaudio
import wikipedia
import speech_recognition as sr
import pyttsx3
import os
import sounddevice
from scipy.io.wavfile import write
import cv2
import time
import imutils

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

def voice_recorder():
    fs=44100
    second = int(input("Enter the time duration in seconds : "))
    record_voice = sounddevice.rec(int(second * fs),samplerate=fs,channels=2)
    sounddevice.wait()
    write("Output.wav",fs,record_voice)
    print("Finished....\nPlease Check it......")

def tellDay():
     
    # This function is for telling the
    # day of the week
    day = datetime.datetime.today().weekday() + 1
     
    #this line tells us about the number
    # that will help us in telling the day
    Day_dict = {1: 'Monday', 2: 'Tuesday',
                3: 'Wednesday', 4: 'Thursday',
                5: 'Friday', 6: 'Saturday',
                7: 'Sunday'}
     
    if day in Day_dict.keys():
        day_of_the_week = Day_dict[day]
        print(day_of_the_week)
        speak("The day is " + day_of_the_week)

def ScreenShot():
    sc=pyautogui.screenshot()
    sc.save('D:\Project Ushwathama\sampless.png') #enter the location/path of destination where the screenshot should be saved.
 
def tellTime():
     
    # This method will give the time
    time = str(datetime.datetime.now())
     
    # the time will be displayed like
    # this "2020-06-05 17:50:14.582630"
    #and then after slicing we can get time
    print(time)
    hour = time[11:13]
    min = time[14:16]
    speak("The time is sir" + hour + "Hours and" + min + "Minutes")

def takeCommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        r.energy_threshold = 700
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
    
        elif "which day it is" in query:
            tellDay()
            continue
         
        elif "tell me the time" in query:
            tellTime()
            continue

        elif 'open youtube' in query:
            speak('Opening Youtube')
            webbrowser.open('youtube.com')
            continue
    
        elif 'open brave' in query:
            speak('Opening Brave')
            webbrowser.open('brave.com')
            continue
        
        elif 'open google' in query:
            speak('Opening Google')
            webbrowser.open('google.com')
            continue

        elif 'open stack overflow' in query:
            speak('Opening Stack Overflow')
            webbrowser.open('stackoverflow.com')
            continue

        elif 'record my voice' in query:
            speak('Recording voice')
            voice_recorder()
            
         elif 'take screenshot' in query:
            speak('Taking Screenshot')
            ScreenShot()
        
        elif 'bye' in query:
            speak('Okay! See you later.')
            exit()
