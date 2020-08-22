# JARVIS-Best-Project

#import some modules
import pyttsx3 #pip install pyttsx3
import datetime #pip install datetime
import speech_recognition as sr #pip install SpeechRecognition
import pyaudio #pip install PyAudio
import wikipedia #pip install wikipedia
import webbrowser #pip install webbrowser
import os #It is a built-in-module
import smtplib #pip install smtplib
import sys #It is a built-in-module

#Store sir in variable master
MASTER = "Sir"


engine = pyttsx3.init()


#define function to speak of your assistant
def speak(audio):
    engine.say(audio)
    engine.runAndWait()

#define time function that tell you time
def time():
    Time = datetime.datetime.now().strftime("%I:%M:%S" )
    speak(Time)

#define time function that tell you date
def date():
    year = int(datetime.datetime.now().year )
    month = int(datetime.datetime.now().month )
    date = int(datetime.datetime.now().day )
    speak(date)
    speak(month)
    speak(year)

#define function to wishme Good-Morning/Good-Afternoon/Good-Evening          
def wishMe():
    speak("Welcome back sir")
    # speak("The current time is")
    # time()
    # speak("The current date is")
    # date()
    hour = datetime.datetime.now().hour
    if hour>=0 and hour<12:
        speak("Good Morning " + MASTER)


    elif hour>=12 and hour<18:
        speak("Good Afternoon " + MASTER)


    else:
        speak("Good Evening " + MASTER)
    speak("I am JARVIS. Please tell me sir how may I help you?")

#define function to take our command
def takeCommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening......")
        r.pause_threshold = 1
        audio = r.listen(source)


    try:
        print("Recognising.....")
        query = r.recognize_google(audio, language='en-in')
        print("Sir you said: ", query)


    except Exception as e:
        print(e)
        speak("Say that again please.....")

        return "None"   
    return query


if __name__ == "__main__":
    wishMe()
    #while true because we maded a quit function in elif
    while True:
    # if 2:#With this he will speak two time and our program is quited
        query = takeCommand().lower()
        if 'wikipedia' in query:
            speak('Searching Wikipedia.....')
            query = query.replace("Wikipedia","")
            results =wikipedia.summary(query, sentences=2)
            speak("According to wikipedia")
            print(results)
            speak(results)


        elif 'open youtube' in query:
            webbrowser.open("youtube.com")


        elif 'open google' in query:
            webbrowser.open("google.com")


        elif 'open stackoverflow' in query:
            webbrowser.open("stackoverflow.com")


        elif 'open anacondanavigator' in query:
            anaconda = 'C:\\Desktop\\Anaconda Navigator (anaconda3).lnk'


        elif 'the time' in query:
            strTime = datetime.datetime.now().strftime("%I:%M:%S")
            speak("Sir the time is" + strTime)


        elif 'open gmail' in query:
            webbrowser.open("gmail.com")


        elif 'vs code' in query:
            path = "C:\\Users\\sai\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe"
            os.startfile(path)


        elif 'chess' in query:
            gamePath = "C:\\Program Files\\Microsoft Games\\Chess\\chess.exe"
            os.startfile(gamePath)


        elif 'purble' in query:
            path = "C:\\Program Files\\Microsoft Games\\Purble Place\\PurblePlace.exe"


        elif 'python idle' in query:
            path = "C:\\Users\\sai\\AppData\\Local\\Programs\\Python\\Python38-32\\Lib\\idlelib\\idle.pyw"


        elif 'time' in query:
            speak("The current time is")
            time()


        elif 'date' in query:
            speak("The current date is")
            date()


        elif 'hello' in query:
            speak("Hello sir. How are you?")
            print("Hello sir. How are you?")


        elif 'I am fine' in query:
            speak("Ok, Sir.")
            print("Ok, Sir.")


        elif 'I am not well' in query:
            speak("Don't use laptop at this time.")
            print("Don't use laptop at this time.")


        elif 'quit' in query:
            sys.exit()
