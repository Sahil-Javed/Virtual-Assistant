import webbrowser
import pyttsx3
import speech_recognition as sr
import datetime
import wikipedia
import webbrowser
import os
import smtplib

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice',voices[0].id)

def speak(audio):
    engine.say(audio) 
    engine.runAndWait()
    
def wishme():
    hour = int(datetime.datetime.now().hour)
    if hour>= 0 and hour<12:
        print('Good Morning!')
        speak('Good Morning!')
    elif hour>= 12 and hour<18:
        print('Good Afternoon!')
        speak('Good Afternoon!')
    else:
        print('Good Evening')
        speak('Good Evening')
        
    print("I am sam sir. Please tell me how may i help you")
    speak("I am sam sir. Please tell me how may i help you")

def takeCommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source)
        
    try:
        print("Recognizing...")
        query = r.recognize_google(audio, language='en-in')
        print(f" User said: {query}\n")
        
    except Exception as e:
        # print(e)
        print("Say that again please...")
        return "None"
    
    return query 
        
def sendEmail(to,content):
    server = smtplib.SMTP('smtp.gmail.com',587)
    server.ehlo()
    server.starttls()
    server.login('sahiljaved01234@gmail.com','fxglmiophkmnaxkw')
    server.sendmail('sahiljaved01234@gmail.com',to,content)
    server.close()
    
if __name__ == "__main__":
    wishme()
    if 1:
        query = takeCommand().lower()
        
        if "wikipedia" in query:
            speak("Searching Wikipedia...")
            query = query.replace("wikipedia","")
            result = wikipedia.summary(query,sentences=2)
            print(result)
            speak(result)
            
        elif 'open youtube' in query:
            webbrowser.open("youtube.com")
            
        elif 'open google' in query:
            webbrowser.open("google.com")
            
        elif 'open facebook' in query:
            webbrowser.open("facebook.com")
            
        elif 'open stackoverflow' in query:
            webbrowser.open("stackoverflow.com")
            
        elif 'play music' in query:
            music = 'F:\\music'
            songs = os.listdir(music)
            print(songs)
            os.startfile(os.path.join(music,songs[0]))
            
        elif 'open code' in query:
            codepath = ("C:\\Users\\admin\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe")
            os.startfile(codepath)
            
        elif ' the time' in query:
            time = datetime.datetime.now().strftime('%H:%M:%S')
            speak(f'Sir, the time is {time}')
            
        elif 'email to fahim' in query:
            try:
                speak("What should I say?")
                content = takeCommand()
                to = "pathanfahim3@gmail.com"    
                sendEmail(to, content)
                speak("Email has been sent!")
            except Exception as e:
                print(e)
                speak("Sorry my friend harry bhai. I am not able to send this email")