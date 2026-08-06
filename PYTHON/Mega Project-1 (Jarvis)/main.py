import speech_recognition as sr
import webbrowser
import pyttsx3
import time
import musiclibrary
import requests
from groq import Groq

recognizer =sr.Recognizer()
engine = pyttsx3.init()
newsapi = "ef907410ef6446b8b6fcc25741cc03bb"
def speak(text):
    engine = pyttsx3.init()
    engine.say(text)
    engine.runAndWait()
    engine.stop()
def aiprocess(command):
    client = Groq(api_key="YOUR_API_KEY")

    chat = client.chat.completions.create(
        model="llama-3.3-70b-versatile",
        messages=[ {"role": "system", "content": "You are a virtual assistant named Jarvis, skilled in general tast like alexa and google cloud."}, 
            {"role": "user", "content": command} ]
        )
    print(chat.choices[0].message.content)
    return chat.choices[0].message.content

def procssCommand(c):
    if "open google" in c.lower():
        speak("Opening Google")
        webbrowser.open("https://google.com")
    elif "open youtube" in c.lower():
        speak("Opening Youtube")
        webbrowser.open("https://youtube.com")
    elif "open instagram" in c.lower():
        speak("Opening Instagram")
        webbrowser.open("https://instagram.com")
    elif "open facebook" in c.lower():
        speak("Opening facebook")
        webbrowser.open("https://facebook.com")
    elif c.lower().startswith("play"):
        speak("Opening songs")
        song = c.lower().split()[1]

        if song in musiclibrary.music:
            webbrowser.open(musiclibrary.music[song])
        else:
            speak("Song not found")
    
    elif "news" in c.lower():
        speak("Opening News")

        r = requests.get(f"https://newsapi.org/v2/top-headlines?country=in&apiKey={newsapi}")

        if r.status_code == 200:
            # Parse the JSON response
            data = r.json()

            # Extract the articles
            articles = data.get("articles", [])

            if articles:
                for article in articles:
                    title = article.get("title", "No Title")
                    print(title)      # Print on terminal
                    speak(title)      # Speak the headline
            else:
                speak("Sorry, no news articles were found.")

        else:
            speak("Sorry, I couldn't fetch the news.")
    
    else:
        output = aiprocess(c)
        speak(output)
        

if __name__ == "__main__":
    speak("Initializing Jarvis....")
    r = sr.Recognizer()
    while True:
        # Listen for the wake word "Jarvis"
        # obtain audio from the microphone

        speak("recognizing...")      
        print("recognizing...")      
        # recognize speech using google
        try:
            with sr.Microphone() as source:
                print("Listening...")
                audio = r.listen(source,timeout=5,phrase_time_limit=8)
                word = r.recognize_google(audio)
                print(f"Recognized: '{word}'")
            

                if (word.lower() == "jarvis"):
                    print("Wake word detected")
                    speak("yeah.... ")
                    
                    # listen for command
                    with sr.Microphone() as source:
                        
                        print("Jarvis Activated...")
                        audio = r.listen(source, timeout=5, phrase_time_limit=8)
                        command = r.recognize_google(audio)
                        procssCommand(command)
                        # if word.lower()== "stop":
                        #     print("end jarvis")
                        #     engine.stop()               


        except Exception as e:
            print("Error; {0} ".format(e))