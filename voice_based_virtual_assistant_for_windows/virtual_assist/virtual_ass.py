#My assistant name>>>> WORKMATE
#some features of workmate
#greetings
#searching wikipedia>>>just say "wikipedia"
#can tell current time,day,date
#open file explorer>>>just say "my computer"
#can tell jokes>>>just say "tell me jokes"
#can tell the questions...a) who are you,b) who created you,c) what can you do
#..............................................................................................
import warnings
import speech_recognition as sr
import pyttsx3
import datetime
import wikipedia
from datetime import date
import pyjokes
import os
import subprocess
import webbrowser
import requests

warnings.filterwarnings("ignore")

wake_word = "workmate"

def speak_text(text):
    engine = pyttsx3.init()
    engine.say(text)    
    rate = engine.getProperty('rate')
    engine.setProperty('rate',rate-200)   
    voices = engine.getProperty('voices')       #getting details of current voice    
    engine.setProperty('voices', voices[0].id)     
    engine.runAndWait()
    
def listen_to_audio():
    # set up the recognizer
    recognizer = sr.Recognizer()
    
    # listen for audio
    with sr.Microphone() as source:
        print("Say something!")
        audio = recognizer.listen(source)
    
    # recognize speech using Google Speech Recognition
    try:
        text = recognizer.recognize_google(audio)
        print("You said: {}".format(text))
        return text
    except sr.UnknownValueError:
        print("Google Speech Recognition could not understand audio")
        return None
    except sr.RequestError as e:
        print("Could not request results from Google Speech Recognition service;".format(e))
        return None    
    
def process_text(text):    
    
    if "workmate" in text.lower():       
        hour=datetime.datetime.now().hour
        
        if hour>=0 and hour<12:
            speak_text("Hello,Good Morning How can help you today?")
            print("Hello,Good Morning How can help you today?")
           
        elif hour>=12 and hour<18:
            speak_text(" Hello, Good Afternoon How Can Help You Today ?")
            print("Hello, Good Afternoon How Can Help You Today ?")
            
        elif hour>=18 and hour<24:
            speak_text("Hello,Good Evening How Can Help You Today ?")
            print("Hello,Good Evening How Can Help You Today ?")
            
        else:
            speak_text("I'm sorry, I didn't understand what you said.")
            print("I'm sorry, I didn't understand what you said.")    
        
    elif "wikipedia" in text.lower():
        speak_text("Hello! welcome to wikipedia")
        print("searching Wikipedia: ")
        text = listen_to_audio() 
        if text is not None:            
            result=wikipedia.summary(text,sentences=3)
            print(result)
            speak_text(result)            
        else:
            speak_text("under construction")            
    
    elif "who are you" in text.lower():
        print("i am workmate, Your assistant")
        speak_text("i am workmate, Your assistant")        
        
    elif "who created you" in text.lower() or "who build you" in text.lower() or "who discovered you" in text.lower():
        print("i was build by Thanigaivel")
        speak_text("i was build by Thanigaivel")        
        
    elif "what can you do" in text:
        print("i am progeammed to minor tasks like opening youtube,chorme,gmail and serach wikipedia,can ask current time and date and more")
        speak_text("i am progeammed to minor tasks like opening youtube,chorme,gmail and serach wikipedia,can ask current time and date and more")
        
    elif "today date" in text.lower() or "what date" in text.lower():
        today=date.today()       
        dtt=today.strftime("%B %d,%y")
        print(dtt)
        speak_text(dtt)
        
    elif "what day" in text.lower():
        day= datetime.datetime.now()      
        tday=day.strftime("%A")
        speak_text(tday)
        print(tday)
        
    elif "what time" in text.lower() or "time now" in text.lower():
        now = datetime.datetime.now()
        current_time = now.strftime("%I:%M:%p") 
        print("current time is: "+current_time)             
        speak_text("current time is:"+current_time)               
    
    elif "tell me jokes" in text.lower() or "tell jokes" in text.lower():
        joke = pyjokes.get_joke()
        print(joke)
        speak_text(joke)
        
    elif "my computer" in text.lower() or "open file explorer" in text.lower():
        FILE_EXPLORER_CMD = "explorer"        
        subprocess.Popen(FILE_EXPLORER_CMD)
        print("will open?")        
        print("File Explorer opened!...")       
            
    elif "stop" in text.lower() or "exit" in text.lower() or "ok bye" in text.lower():
        print("okay Byee")
        speak_text("okay Byee")
        exit()
        
    elif "open youtube" in text.lower():
        webbrowser.open_new_tab("https://www.youtube.com")
        speak_text("youtube is open now")
        print("youtube is open now")
        
              
    elif 'open google' in text.lower():
            webbrowser.open_new_tab("https://www.google.com")
            speak_text("Google chrome is open now!")
            print("Google chrome is open now!")
            
    elif 'open gmail' in text.lower():
            webbrowser.open_new_tab("gmail.com")
            speak_text("GMail open now!")
            print("GMail open now!")
            
    elif "open notepad" in text.lower():
        app_name = "notepad.exe"
        subprocess.call(app_name)
        print("opened")
        speak_text("opened")
            
    elif "log off" in text.lower() or "sign out" in text.lower():
            speak_text("Ok , your pc will log off in 10 sec make sure you exit from all applications")
            subprocess.call(["shutdown", "/l"])
            
    else:
        speak_text("I don't Know that")
        print("I don't Know that")

if __name__ == "__main__":
    
    while True:
        text = listen_to_audio()
              
        if text is not None:
            process_text(text)
            continue
        
        

        
        
   
    
