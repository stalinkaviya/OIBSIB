import pyttsx3 as p
import speech_recognition as sr
import datetime
import wikipedia
import webbrowser
  
engine = p.init()
rate = engine.getProperty('rate')
engine.setProperty('rate',130)
voices = engine.getProperty('voices')
engine.setProperty('voice',voices[1].id)



def speak(text):
   engine.say(text)
   engine.runAndWait()


r = sr.Recognizer()
   
speak("Hello mam iam your voice assistant, how are you")   

with sr.Microphone() as source:
   r.energy_threshold=10000
   r.adjust_for_ambient_noise(source,1.2)
   print("listening....")
   audio = r.listen(source)
   text=r.recognize_google(audio)
   print(text)

if "what" and "about" and "you" in text:
   speak('iam having a good day mam')
speak('what can i do for you')

def wishMe():
   hour = int(datetime.datetime.now().hour)
   if hour>=0 and hour<12:
      speak("Good Morning!")

   elif hour>=12 and hour<18:
      speak("Good Afternoon!")

def takecommand():
   
   r = sr.Recognizer()
   with sr.Microphone()as source:
      print("Listening...")
      audio = r.listen(source)

while True:
   query = takecommand().lower()

   #Logic for executing tasks based on query
   if 'wikipedia' in query:
      speak('searching wikipedia...')
      query = query.replace("wikipedia","")
      results = wikipedia.summary(query, sentences=2)
      speak(results)
      print(results)

   elif 'open youtube' in query:
      webbrowser.open("youtube.com")

   elif 'open google' in query:
      webbrowser.open("google.com")
      


