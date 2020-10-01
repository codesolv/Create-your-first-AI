import pyttsx3  # pip install pyttsx3
import speech_recognition as sr  # pip install speechRecognition
import datetime
import subprocess
from playsound import playsound #pip install playsound
import wikipedia  # pip install wikipedia
import webbrowser
import os

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id) #you can change the voice


def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def seach_google(): #this will search your voice in Google
    playsound("2.mp3")
    sr.Microphone(device_index=1)
    r = sr.Recognizer()

    r.energy_threshold = 5000
    with sr.Microphone() as source:
        speak("what u want to search")
        print("lisenting.....")
        audio = r.listen(source)
        try:
            text = r.recognize_google(audio)
            print(f"User said: {text}\n")
            url = 'https://www.google.com/search?q='
            search_url = url + text
            webbrowser.open(search_url)
        except:
            speak("say it again")

def backgroundsong(): #play a song in background using this
    playsound("first.mp3") #you can any other song

def wishMe(): #this function wish you accoding to time and you can put your name instead of user
    hour = int(datetime.datetime.now().hour)
    if hour >= 0 and hour < 12:
        speak("Good Morning! user")

    elif hour >= 12 and hour < 18:
        speak("Good Afternoon! user")

    else:
        speak("Good Evening! user ")

    speak("time is :")
    strTime = datetime.datetime.now().strftime("%H 'hour' %M 'minutes' %S 'second'")
    speak(F"the time is:{strTime}")

    speak("I am jarvics. Your personal virtual assistant . version 2.0.2.0.1 .  made by sourav. Please tell me how may I help you") #you can change it


def takeCommand():
    # It takes microphone input from the user and returns string output

    r = sr.Recognizer()

    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source)
    try:
        print("Recognizing...")
        query = r.recognize_google(audio, language='en-in')
        print(f"User said: {query}\n")

    except Exception as e:
        print("Say that again please...")
        return "None"
    return query

if __name__ == "__main__":
    backgroundsong()
    wishMe()
    while True:

        query = takeCommand().lower() #take voice command form user

        # Search something in wikipedia
        if 'wikipedia' in query:
            speak('Searching Wikipedia...')
            query = query.replace("wikipedia", "")
            results = wikipedia.summary(query, sentences=3)
            speak("According to Wikipedia")
            print(results)
            speak(results)

        elif 'open youtube' in query:
            #webbrowser.open("youtube.com")
            webbrowser.open("youtube.com")

        elif 'open facebook' in query:
            webbrowser.open("facebook.com")

        elif 'open twitter' in query:
            webbrowser.open("twiter.com")

        elif 'open stackoverflow' in query:
            webbrowser.open("stackoverflow.com")

        elif 'open instragram' in query:
            webbrowser.open("www.instagram.com")

        elif 'open google map' in query:
            webbrowser.open("www.google.com/maps")


        elif 'open zomato' in query:
            webbrowser.open("zomato.com")

        elif 'who are you' in query:
            speak("i am jarvis. i am a AI. made by sourav")

        elif 'how are you' in query:
            speak("i am good . how are you .")

        elif 'i am fine' in query:
            speak("ok")

        elif 'open swiggy' in query:
            webbrowser.open("swiggy.com")

        elif 'open notepad' in query:
            subprocess.Popen('C:\\Windows\\System32\\notepad.exe')

        elif 'open whatsapp' in query:
            webbrowser.open("whatsapp.com")

        elif 'play music' in query:
            music_dir = 'A:\\fav music' #use your own music directry
            songs = os.listdir(music_dir)
            os.startfile(os.path.join(music_dir, songs[0]))


        elif 'open notepad' in query:
            subprocess.Popen('C:\\Windows\\System32\\notepad.exe')

        elif 'open cmd' in query:
            os.system("start /wait cmd /c {cd /../}")


        elif 'want to search in google' in query:
            seach_google()
        
        # Hey!, as I can see that you did a great job in thi AI!
        # U have written clean code define useful functions
        # But I will suggest you some changes in your code, hope u like them
        
        elif 'open notepad and quit' in query:
            subprocess.Popen('C:\\Windows\\System32\\notepad.exe')
        # as u can see that here i have included a function to open notepad and quit
        # this will help u as it sometimes becames very annoying that after doing a task with this AI your AI does'nt close and it keeps working in background
        # but u will also need this feature sometimes soo..
        # by this function u can say to this task and quit or if u don't want to do soo u can just say do this task
        # And u can can implement this feature with all your function
        # Hope this may help u!
        # I did spent a lot of time thinking about this function please accept this pull request!
        # Thanks and Peace!


        elif 'quit' in query:
            exit(0)
             
                #Code By Sourav

    
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        #By Sourav
