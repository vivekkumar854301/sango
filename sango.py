import pyttsx3
import speech_recognition as sr
import datetime
import wikipedia
import  webbrowser
import os
import smtplib

 
engine =pyttsx3.init('sapi5')
voices= engine.getProperty('voices')
# print(voices[2].id)
engine.setProperty('voice',voices[2].id)


def speak(audio):
    engine.say(audio)
    engine.runAndWait()
    
def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        speak("Good morning dear !")
    elif hour>=12 and hour<18:
        speak("Good Afternoon dear !")
    else:
        speak("Good evening dear ! ")
        
    speak("I am sango sir. please tell me how my i help you ")

def takeCommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening.....")
        r.pause_threshold = 1
        audio = r.listen(source)
        
    try:
        print("Recognizing...")
        query = r.recognize_google(audio,language='en-in')
        print(f"user said: {query}\n")
        
    except Exception as e:
        #print(e)
        
        speak("say that again please ... ")
        print("say that again please....")
        return "None"
    return query

def sendEmail(to, content):
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.login('youremail@gmail.com', 'your-password')
    server.sendmail('youremail@gmail.com', to, content)
    server.close()
    
    
if __name__ == "__main__":
    wishMe()
    while True:
    #if 1:
        query=takeCommand().lower()
        if 'wikipedia' in query:
            speak('Searching wikipedia......')
            query=query.replace("wikipedia","")
            results=wikipedia.summary(query,sentences=2)
            speak("According to wikipedia")
            print(results)
            speak(results)
        
        elif 'open youtube' in query:
            webbrowser.open("youtube.com")
        
        elif 'open google' in query:
            webbrowser.open("google.com")
            
        elif 'open linkedin' in query:
            webbrowser.open("linkedin.com")
        
        elif 'open instagram' in query:
            webbrowser.open("instagram.com")
            
        elif 'play song' in query:
            webbrowser.open("jiosaavn.com")
            
        elif 'play music ' in query:
            music_dir = 'F:\sad song'
            songs =os.listdir(music_dir)
            print(songs)
            os.startfile(os.path.join(music_dir,songs[0]))
        
        elif 'the time' in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")    
            speak(f"Sir, the time is {strTime}")
            
        elif 'open vs code' in query:
            codepath ="D:\Microsoft VS Code\Code.exe"
            os.startfile(codepath)
            
        elif 'send Email' in query:
            try:
                speak("what should i say?")
                contect=takeCommand()
                to = "viveksingh144399@gmail.com"
                sendEmail(to,contect)
                speak("Email has been sent!")
            except Exception as e:
                print(e)
                speak("sorry my friend . i am not able to send this email")
                
            
            
              