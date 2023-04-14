import pyttsx3
import datetime
import speechRecognition as sr


 
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
    
    
if __name__ == "__main__":
    wishMe()
    takeCommand()