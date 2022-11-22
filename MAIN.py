import speech_recognition as sr
import pyttsx3
import datetime
import wikipedia
import webbrowser
import os
import time
import subprocess
from ecapture import ecapture as ec
import wolframalpha
import json
import requests
import sys


engine=pyttsx3.init('sapi5')
voices=engine.getProperty('voices')
engine.setProperty('voice','voices[0].id')

def speak(text):
    engine.say(text)
    engine.runAndWait()

def wishMe():
    hour=datetime.datetime.now().hour
    if hour>=0 and hour<12:
        speak("Hello,Good Morning")
        print("Hello,Good Morning")
    elif hour>=12 and hour<18:
        speak("Hello,Good Afternoon")
        print("Hello,Good Afternoon")
    else:
        speak("Hello,Good Evening")
        print("Hello,Good Evening")


def note(text):
    date = datetime.datetime.now()
    file_name = str(date).replace(":", "-") + "-note.txt"
    with open(file_name, "w") as f:
        f.write(text)

    subprocess.Popen(["notepad.exe", file_name])




def takeCommand():
    r=sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        audio=r.listen(source)

        try:
            statement=r.recognize_google(audio,language='en-in')
            print(f"user said:{statement}\n")

        except Exception as e:
            speak("Pardon me, please say that again")
            return "None"
        return statement

print("Loading your AI personal assistant esper")
speak("Loading your AI personal assistant esper")
wishMe()


if __name__=='__main__':
    while True:
        speak("Tell me how can I help you now?")
        statement = takeCommand().lower()
        if statement==0:
            continue



        if 'open wikipedia' in statement:
            speak('Searching Wikipedia...')
            webbrowser.open_new_tab("https://www.wikipedia.org/")
            speak("wikipedia is open now")

        elif 'open youtube' in statement:
            webbrowser.open_new_tab("https://www.youtube.com")
            speak("youtube is open now")
            time.sleep(5)

        elif 'open google' in statement:
            webbrowser.open_new_tab("https://www.google.com")
            speak("Google chrome is open now")
            time.sleep(5)

        elif 'open gmail' in statement:
            webbrowser.open_new_tab("https://mail.google.com/mail/u/0/#inbox")
            speak("Google Mail open now")
            time.sleep(5)

        elif 'time' in statement:
            strTime=datetime.datetime.now().strftime("%H:%M:%S")
            speak(f"the time is {strTime}")


        elif 'news' in statement:
            news = webbrowser.open_new_tab("https://timesofindia.indiatimes.com/?from=mdr")
            speak('Here are some headlines from the Times of India,Happy reading')
            time.sleep(6)

        elif "camera" in statement or "take a photo" in statement:
            ec.capture(0,"robo camera","img.jpg")

        elif 'search'  in statement:
            statement = statement.replace("search", " ")
            webbrowser.open_new_tab(statement)
            time.sleep(5)

        elif 'who are you' in statement or 'what can you do' in statement:
            speak('I am esper your personal assistant. I am programmed to minor tasks like'
                  'opening youtube,google chrome, gmail, predict time, take a photo, search wikipedia, predict weather' 
                  'In different cities, get top headline news from times of india ')


        elif "who made you" in statement or "who created you" in statement or "who discovered you" in statement:
            speak("I was built by Harshit and Kartikey")
            print("I was built by Harshit and Kartikey")

        elif 'make a note' in statement:
                statement = statement.replace("make a note", "")
                note(statement)
       
        elif "exit" in statement or "quit" in statement :
             speak("PEACE OUT")
             exit()

    note("manually exit today's notes")
