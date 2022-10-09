import os
import cv2
import time
import imutils
import pyaudio
import pyttsx3
import calendar
import wikipedia
import pyautogui
import webbrowser
import sounddevice
from ast import main
from tkinter import *
from datetime import datetime
import speech_recognition as sr
from scipy.io.wavfile import write

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice',voices[0].id)

#Function to make USHVATHAMA speak
def speak(audio):
    engine.say(audio)
    engine.runAndWait()


#Function to wish the user
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
    speak('Enter the time duration in seconds')
    fs=44100
    second = int(input("Enter the time duration in seconds : "))
    speak('Recording voice')
    record_voice = sounddevice.rec(int(second * fs),samplerate=fs,channels=2)
    sounddevice.wait()
    write("Output.wav",fs,record_voice)
    print("Finished....\nPlease Check it......")

def ScreenShot():
    sc=pyautogui.screenshot()
    sc.save('D:\Project Ushwathama\sampless.png')

def takePicture():
    cap = cv2.VideoCapture(0)
    ret, frame = cap.read()
    (grabbed, frame) = cap.read()
    showimg = frame
    cv2.imshow('img1', showimg)  # display the captured image
    cv2.waitKey(1)
    time.sleep(0.3) # Wait 300 miliseconds
    image = 'D:\Project Ushwathama\photo.png'
    cv2.imwrite(image, frame)
    cap.release()
    return image

def tellDay():
     
    # This function is for telling the
    # day of the week
    day = datetime.today().weekday() + 1
     
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
 
 
def tellTime():
     
    # This method will give the time
    time = str(datetime.now())
     
    # the time will be displayed like
    # this "2020-06-05 17:50:14.582630"
    #and then after slicing we can get time
    print(time)
    hour = time[11:13]
    min = time[14:16]
    speak("The time is " + hour + "Hours and" + min + "Minutes")

def takeCommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        r.energy_threshold = 200
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


def Calendar():
    
    speak('Please enter the year of the calendar you want to see')

    def showCalendar():
        gui = Tk()
        gui.config(background = 'black')
        gui.title("Calender of the year")
        gui.geometry("1000x1000")
        year = int(year_field.get())
        gui_content= calendar.calendar(year)
        calYear = Label(gui, text= gui_content, font= "Consolas 10 bold")
        calYear.grid(row=5, column=1,padx=20)
        gui.mainloop()

    new = Tk()
    new.config(background='black')
    new.title('CALENDER')
    new.geometry("300x300")
    cal = Label(new, text="Calender", bg="grey",font=("times",28,"bold"))
    year = Label(new, text="Enter year", bg='dark grey')
    year_field = Entry(new)
    button = Button(new, text='Show Calender', fg='Black', bg='grey', command = showCalendar)
    Exit = Button(new, text='Exit', fg='Black', bg='grey', command = exit)

    cal.grid(row=1, column=1)
    year.grid(row=3, column=1)
    year_field.grid(row=5, column=1)
    button.grid(row=7, column=1)
    Exit.grid(row=9, column=1)
    new.mainloop()

def generate_Password():
    lower = "abcdefghijklmnopqrstuvwxyz"
    upper = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    numbers = "0123456789"
    symbols = "!@#$%^&*()_-[]{}:;<>,.?"
    all = lower + upper + numbers + symbols
    speak("Please enter the length of the password according to your preferences")
    length = int(input("Please enter the length of the password according to your preferences : "))
    password = "".join(random.sample(all,length))
    speak("The password generated is on your screen")
    print("The password generated is : ",password)
    print()
    
# Program starts here
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
            print("According to Wikipedia...\n")
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
            webbrowser.open('https://youtube.com')
            continue

        elif 'open spotify' in query:
            speak('Opening Spotify')
            webbrowser.open('https://open.spotify.com/')
            continue
    
        elif 'open brave' in query:
            speak('Opening Brave')
            webbrowser.open('https://brave.com')
            continue
        
        elif 'open google' in query:
            speak('Opening Google')
            webbrowser.open('https://google.com')
            continue

        elif 'open stack overflow' in query:
            speak('Opening Stack Overflow')
            webbrowser.open('https://stackoverflow.com')
            continue

        elif 'record my voice' in query:
            voice_recorder()

        elif 'take screenshot' in query:
            speak('Taking screenshot')
            ScreenShot()
            speak('Screenshot taken and successfully saved!!!')
            
        elif 'take photo' in query:
            speak('Taking photo! Look into the camera and smile')
            takePicture()

        elif 'open calendar' in query:
            speak('Opening Calender')
            Calendar()
        
        elif 'generate a new password for me' in query:
            speak('Generating a new password')
            generate_Password()

        elif 'bye' in query:
            speak('Bye Bye! See you later.')
            exit()
