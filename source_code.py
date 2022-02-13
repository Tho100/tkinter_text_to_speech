import pyttsx3
import tkinter as tk
from tkinter import *

window = Tk()
window.title('Text To Speech')
window.geometry('300x200')

input = tk.Entry(window)
input.pack()

txt_speech = pyttsx3.init()

def convert_to_speech():
    speech = str(input.get()) # Get entry input 
    txt_speech.say(speech) # Say the input text
    txt_speech.runAndWait()

button = tk.Button(window,text='Convert To Speech',command=convert_to_speech)
button.pack()

window.mainloop()
