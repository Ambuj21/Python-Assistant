import pyttsx3
import datetime
import wikipedia
import random
import os
import pywhatkit
import webbrowser
import speech_recognition as sr
engine = pyttsx3.init('sapi5')#microsoft developed Api
voices = engine.getProperty('voices') #getting deatils of current voice
engine.setProperty('voices', voices[0])#id use to select diffrent voices 0 for male and 1 for female

def speak(audio):
    engine.say(audio)
    engine.runAndWait()# without this we cannto hear the voice
def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour > 0 and hour < 12:
        print("Good Morning Sir")
    elif hour>=12 and hour < 18:
        speak("Good Afternoon Sir")
    else:
        speak("Good Evening Sir")
    speak("I am your personal assistant. how can i help you")
def command():
    # it takes microphoen input from the user
    s = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening..")
        s.pause_threshold = 0.6
        audio = s.listen(source)
    try:
        print("Recognizing...")
        query = s.recognize_google(audio, language='en-in')
    except Exception as e:
        print("Say that again")
        return "None"
    print(query)
    return query
if __name__ == "__main__":
    wishMe()
    while True:
    # if 1:
        query = command().lower()
        r = list(map(str, query.split(' ')))
        # Logic for executing tasks based on query
        if 'wikipedia' in query:
            speak(f'Searching {query} on Wikipedia...')
            query = query.replace("wikipedia", "")
            results = wikipedia.summary(query, sentences=2)
            speak("According to Wikipedia")
            speak(results)

        elif 'open youtube' in query:
            webbrowser.open("youtube.com")

        elif 'open google' in query:
            webbrowser.open("google.com")

        elif 'open stackoverflow' in query:
            webbrowser.open("stackoverflow.com")   

        elif 'song' in r:
             music = 'C:\\Users\\ambuj kumar\\Music'
             n = random.randint(0, 80)
             songs = os.listdir(music)
             os.startfile(os.path.join(music, songs[n]))
        elif 'open codechef' in query:
            webbrowser.open("https://www.codechef.com/contests/?itm_medium=navmenu&itm_campaign=allcontests_head")
        
        elif 'what is the time' in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")    
            speak(f"the time is {strTime}")
        elif 'say' in r or 'hi' in r:
            speak(f"hii {r[-1]}")
        elif "send" in r or 'message' in r:
            speak("to whom")
            n = '+91'+command()
            speak("And what is the message sir")
            m = command()
            speak("hour")
            h = int(command())
            speak("minute")
            mi = int(command())
            pywhatkit.sendwhatmsg(n, m, h, mi)
        elif 'exit' in r or "bye" in r:
            speak("Ok sir! Good Bye")
            exit()
        else:
            speak("Next Command sir")