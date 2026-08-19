import pyttsx3
import time

engine = pyttsx3.init()

engine.say("Initializing Jarvis")
engine.runAndWait()

time.sleep(2)

engine.say("Hello again")
engine.runAndWait()