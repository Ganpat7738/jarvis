from tkinter import *
import pyttsx3  # pip install pyttsx3
import speech_recognition as sr  # pip install speechRecognition
import datetime
import wikipedia  # pip install wikipedia
import webbrowser
import os


root = Tk()
root.geometry("600x600")
canvas = Canvas(root, width = 550, height = 550)
canvas.pack()
img = PhotoImage(file="C:\Users\Ganpat\Desktop\jarvis\jarvis.png")
canvas.create_image(20,20, anchor=NW, image=img)


def jar():
    engine = pyttsx3.init('sapi5')  # it takes the voice from windows
    voices = engine.getProperty('voices')
    # print(voices[1].id)
    engine.setProperty('voice', voices[0].id)

    def speak(audio):
        engine.say(audio)
        engine.runAndWait()

    def wishMe():
        hour = int(datetime.datetime.now().hour)
        if hour >= 0 and hour < 12:
            speak("Good Morning!")

        elif hour >= 12 and hour < 18:
            speak("Good Afternoon!")

        else:
            speak("Good Evening!")

        speak("I am Jarvis Sir. Please tell me how may I help you ")

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
            # print(e)
            print("Say that again please...")
            return "None"
        return query

    if __name__ == "__main__":
        speak(" Activating jarvis ")
        wishMe()
        while True:

            query = takeCommand().lower()

            # Logic for executing tasks based on query
            if 'wikipedia' in query:
                speak('Searching Wikipedia...')
                query = query.replace("wikipedia", "")
                results = wikipedia.summary(query, sentences=2)
                speak("According to Wikipedia")
                print(results)
                speak(results)

            elif 'open youtube' in query:
                speak(" opening youtube ")
                webbrowser.open("youtube.com")

            elif 'open google' in query:
                speak(" opening google ")
                webbrowser.open("google.com")

            elif 'open whatsapp' in query:
                speak(" opening whatsapp ")
                webbrowser.open("web.whatsapp.com")


            elif 'play music' in query:
                speak(" Playing music for you . Enjoy your music ")
                music_dir = 'C:\Users\Ganpat\Desktop\jarvis\jarvis\songs'
                songs = os.listdir(music_dir)
                print(songs)
                os.startfile(os.path.join(music_dir, songs[0]))

            elif 'open document' in query:
                speak(" opening document ")
                music_dir = 'C:\Users\Ganpat\Desktop\jarvis\jarvis\docx'
                doc = os.listdir(music_dir)
                print(doc)
                os.startfile(os.path.join(music_dir, doc[0]))


            elif 'the time' in query:
                strTime = datetime.datetime.now().strftime("%H:%M:%S")
                speak(f"Sir, the time is {strTime}")

            elif 'open Chrome' in query:
                codePath = "C:\Program Files (x86)\Google\Chrome\Application\chrome.exe"
                os.startfile(codePath)

            elif 'quit' in query or 'bye' in query or 'deactivate' in query:
                speak("Power mode off")
                exit()



f1=Frame(root , borderwidth= 5 , bg="red" , relief=SUNKEN)
f1.pack()

btn= Button(root , text="start jarvis" , padx=20 , pady=20 , command= jar)
btn.pack()

root.mainloop()