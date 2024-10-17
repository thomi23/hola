from tkinter import* 
import speech_recognition as sr
import webbrowser
import pyttsx3
from datetime import datetime
import subprocess

root = Tk()
root.geometry("500x500")
root.title("comvertidor")

welcome = Label(root,text="bienvenido a tu asistente personal")
welcome.place(relx=0.5,rely=0.1,anchor=CENTER)

txt_voice = pyttsx3.init() 

def speek(audio):
    txt_voice.say(audio)
    txt_voice.runAndWait()
    

def r_audio():
    speech_recognisor = sr.Recognizer()
    speek("hola en que te ayudo")
    with sr.Microphone() as source:
        audio = speech_recognisor.listen(source)
        voice_data =""
        try:
           voice_data = speech_recognisor.recognize_google(audio,language = "esu")
        except sr.UnknownValueError:
           print("por favor repite no entendi tu solicitud")
           speek("porfavor repite no entendi tu solicitud")
           r_audio()
    commands(voice_data)

def commands(voice_data):
    print(voice_data)
    if "nombre" in voice_data:
        speek("mi nombre es stiven")
        print("mi nombre es stiven")
    if "que hora es" in voice_data:
        time = datetime.now()
        format_time = time.strftime("%H:%M:%S")
        speek("la hora es"+ format_time)
        print("la hora es" + format_time)
    if "buscar" in voice_data:
        speek("abriendo google")
        print("abriendo google")
        webbrowser.get().open("https://google.com/")
    if "ver videos" in voice_data:
         speek("abriendo youtube")
         print("abriendo youtube ")
         webbrowser.get().open("https://youtube.com/")    
    if "abrir editor de texto" in voice_data:
         speek("abriendo editor de texto")
         print("abriendo editor de texto ")
         subprocess.Popen(['notepad.exe'])    
   
    
   
    
btn = Button(root,text="iniciar",command=r_audio)   
btn.place(relx=0.5,rely=0.5,anchor=CENTER) 


root.mainloop()    