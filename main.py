import pyttsx3 #pip install pyttsx3
import speech_recognition as sr #pip install speechRecognition
import datetime
import wikipedia #pip install wikipedia
import webbrowser
import os
import smtplib


print("Initializing Nova")
MASTER ="Aryaa"
engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice',voices[0].id)
# Speak function will pronounce the string which is passed to it
def speak(text):
    engine.say(text)
    engine.runAndWait()

# This function will wish you as per the current time
def wishMe():
    hour = int(datetime.datetime.now().hour)

    if hour>=0 and hour<12:
        speak("Good Morning"+ MASTER)
    elif hour>=12 and hour<18:
        speak("Good Afternoon"+ MASTER)
    else:
        speak("Good Evening"+ MASTER)
    speak("Hello...I am Nova...How may I help you?")

# This function will take command from the microphone
def takeCommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        audio = r.listen(source)

    try:
        print("Recognizing...")
        query = r.recognize_google(audio, language = 'en-in')
        print(f"user said: {query}\n")

    except Exception as e:
        print("Say that again please")
        query = None
    return query


                 
# Main program start here...
def main():
        #speak("Initializing Jarvis...")
    wishMe()
    query = takeCommand()

    # Logic for executing tasks as per the query
    if 'wikipedia' in query.lower():
        speak('searching wikipedia...')
        query = query.replace("wikipedia","")
        results = wikipedia.summary(query,sentences=2)
        print(results)
        speak(results)
        
    elif 'open youtube' in query.lower():
        webbrowser.open("youtube.com")
        
    elif 'open google' in query.lower():
        webbrowser.open("google.com")
    
    elif 'open reddit' in query.lower():
        webbrowser.open("reddit.com")
        
    elif 'play music' in query.lower():
        songs_dir= "C:\\Users\\Divyanshi Rahangdale\\Desktop\\musicc"
        songs = os.listdir(songs_dir)
        print(songs)
        os.startfile(os.path.join(songs_dir,songs[0]))

    elif 'the time' in query.lower():
        strTime = datetime.datetime.now().strftime("%H:%M:%S")
        speak(f"{MASTER} the time is{strTime}")
        
main()
