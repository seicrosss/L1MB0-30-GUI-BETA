import time
import tkinter as tk
from tkinter import*
import threading

from PIL import Image,ImageTk
from Clases.InputComandos import ComandosI
from Clases.Speechmodule import SpeechModule
from Clases.VoiceRecognitionModule import VoiceRecognitionModule

usu="seicros"
usu1="SeicroS"
no="Funcion en desarrollo"
name = "limbo"
name0="Limbo"
name1="L1MB0"

speech = SpeechModule()
recognition = VoiceRecognitionModule()
comando= ComandosI()

def actualizar():
    raiz.update()
    time.sleep(1)

def stars():
    state.set("ON")
    L.set("*" + name1 + " escuchando")
    speech.talk("Iniciada, " + usu)
    while True:

        text = recognition.recognize()
        if text:

            if name in text or name0 in text:
                speech.talk("Si, " + usu)
                L.set("*" + name1 + " escuchando")
                text = recognition.recognize()
                comando.comando(text)
                L.set("*" + name1 + " En comandos")
        L.set("*"+name1+" en reposo")


raiz=Tk()
raiz.title("L1MB0")
raiz.resizable(0,0)
raiz.config(bg="black")
raiz.iconbitmap("1.ico")

state=StringVar()
state.set("OFF")
L=StringVar()
L.set("*ZZZ")

# Carga el gif animado
image = Image.open("n1.gif")
frames = []
for i in range(image.n_frames):
    image.seek(i)
    frames.append(ImageTk.PhotoImage(image.copy()))

# Crea un widget Canvas y coloca el gif animado en el fondo
canvas = tk.Canvas(raiz, width=image.width, height=image.height)
background = canvas.create_image(0, 0, image=frames[0], anchor=tk.NW)
canvas.pack()

# Actualiza el frame del gif cada 100 milisegundos
frame_number = 0
def update_frame():
    global frame_number
    frame_number = (frame_number + 1) % len(frames)
    canvas.itemconfigure(background, image=frames[frame_number])
    raiz.after(100, update_frame)


thread1 = threading.Thread(target=actualizar)
thread2 = threading.Thread(target=stars)

etiqueta = tk.Label(raiz, textvariable=state, bg="black", fg="white",font=("",50))
etiqueta.place(x=210,y=160)
etiqueta1 = tk.Label(raiz, textvariable=L, bg="black", fg="white",font=("",35), bd=0)
etiqueta1.place(x=0, y=0)

boton=tk.Button(raiz, text="Iniciar", command=thread2.start, width=9, height=2, bg="red", fg="black",font=("",20)).place(x=180, y=300)

thread1.start()
raiz.after(100, update_frame)
raiz.mainloop()
