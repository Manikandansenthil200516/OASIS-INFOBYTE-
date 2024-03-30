import speech_recognition as sr
import pyttsx3
import datetime
import webbrowser
import urllib.parse
import webbrowser

import webbrowser 

def speak(text):
    engine.say(text)
    engine.runAndWait()

def hear():
    with sr.Microphone() as source:
        print("Listening...")
        recognizer.adjust_for_ambient_noise(source)  
        audio = recognizer.listen(source)

    try:
        print("Recognizing...")
        query = recognizer.recognize_google(audio)
        return query.lower()
    except sr.UnknownValueError:
        speak(" Sorry  sir, I couldn't understand what you said.")
        return ""
    except sr.RequestError as e:
        speak(f"Could not request results from Google Speech Recognition service; {e}")
        return ""

def welcome():
    hour = datetime.datetime.now().hour

    if 0 <= hour < 12:
        speak("Good morning!")

    elif 12 <= hour < 18:
        speak("Good afternoon!")

    else:
        speak("Good evening!")

    speak("How can I assist you?")

def execute_command(command):
    if "hey " in command:
        speak("Yes, I'm here!")
   
    elif "search" in command:
        search_query = command.split("search")[-1].strip()
        speak(f"Searching for {search_query} on the web...")
        search_web(search_query)

    elif 'open youtube' in command:
        speak("Opening YouTube.")
        webbrowser.open('https://www.youtube.com')

    elif 'open google' in command:
        speak("Opening Google.")
        webbrowser.open("https://www.google.com")

    elif 'play music' in command:
        speak("Sure, which music would you like to play?")
        music_query = hear().lower()
        if music_query:
            speak(f"Playing {music_query} on Spotify.")
        
        else:
            speak("Sorry, I couldn't understand the music you mentioned.")
    elif 'time' in command:
        now = datetime.datetime.now().strftime("%H:%M:%S")
        speak(f"The time is {now}")

    elif 'date' in command:
        now = datetime.datetime.now().strftime("%D-%m-%Y")
        speak(f"The date is {now}")

    
    elif "open LinkedIn" in command:
        speak("Opening your LinkedIn profile.")
        webbrowser.open("https://www.linkedin.com/in/manikandan-senthil-b1255a276/")

    
    elif "open Chat G P T" in command:
        speak("Opening ChatGPT website.")
        webbrowser.open("https://openai.com/blog/chatgpt/")


    elif "open Black box" in command:
        speak("Opening Blackbox/AI website.")
        webbrowser.open("https://www.blackbox.ai/")

    elif "repeat with me" in command:
        text = command.replace("repeat with me", "").strip()
        speak(f"I'm repeating: {text}")

    elif 'exit' in command:
        speak("Thank you, goodbye!")
        exit()

    else:
        speak("I'm sorry sir, I couldn't understand your command.")

def search_web(query):
    encoded_query = urllib.parse.quote_plus(query)
    url = "https://www.google.com/search?q=" + encoded_query
    webbrowser.open(url)

if __name__ == "__main__":
    engine = pyttsx3.init()
    recognizer = sr.Recognizer()

    welcome()

    while True:
        command = hear().lower()
        if command:
            execute_command(command)