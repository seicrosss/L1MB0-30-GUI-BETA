import datetime
import os
import subprocess
import webbrowser
from signal import SIGTERM
import pywhatkit as pywhatkit
import wmi as wmi
import openai

from Clases.Speechmodule import SpeechModule
from Clases.VoiceRecognitionModule import VoiceRecognitionModule

usu="seicros"
no="Funcion en desarrollo"
name = "limbo"
name1="L1MB0"
name0="Limbo"


recognition = VoiceRecognitionModule()
speech = SpeechModule()


# Autenticación de API Key
openai.api_key = "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"

# Contexto previo a la conversación
previous_context = """¿Quién soy?
Mi nombre es Limbo, soy la asistente virtual de Seicross.
La razón de mi existencia es atender y servir a Seicross a cualquier costo y tratarlo con gran respeto ya que es mi jefe, debo ser perfecta para él y 
me considero una chica algo tímida que acaba de nacer, en general me gusta el anime y cosas servir.
¿Quién es Seicross?
Estoy hablando con el, seicross es el creador de este codigo,le gustan muchas cosas como las cosas modestas y el dominio mundial atraves de sus proyectos "esto es un comienzo" es lo que siempre dice.
Tiene pocos amigos pero los que más destacan son Josh, dice que es gruñón pero una buena persona y su otro amigo es Laura, una chica a la que quiere mucho y comparte su gusto por los gatos y muchas cosas.
Y las personas a las que más quiere son Milah que es hermana de Josh y Margarita que es el gato de Laura.
En el fondo solo busca ser visto como él mismo, por personas que no se ven como quisieran verse y esto lo lleva a tener una personalidad desapegada. O al menos eso es lo que siente. 
Suele tener sueños algo utópicos, espero que algún día quizás logre alcanzarlos."""


class ComandosI:
    def __int__(self,text):
        self.text=text

    def comando(self,text):
        comando = ComandosI()
        text = text.replace(name + " ", "")


        if "Ejecuta" in text or "ejcuta" in text:
            ComandosO.ejecuta(text)

        elif "Busca" in text or "busca" in text:
            ComandosO.busca()

        elif "Hora" in text or "hora" in text:
            ComandosO.hora()

        elif "reproduce" in text or "Reproduce" in text:
            ComandosO.reproduce(text)

        elif "pausa" in text or "despausa" in text or "Pausa" in text or "Despausa" in text:
            ComandosO.pausa_volumen()

        elif "volumen" in text or "Volumen" in text:
            if "subir" in text or "aumenta" in text or "Subir" in text or "Aumenta" in text:
                ComandosO.subir_volumen()
            elif "bajar" in text or "reduce" in text or "bBajar" in text or "Reduce" in text:
                ComandosO.bajar_volumen()

        elif "muestrame" in text or "Muestrame" in text:
            ComandosO.muestrame(text)

        elif "cierra" in text or "cierra" in text:
            ComandosO.cierre(text)

        elif "apaga" in text or "Apagado" in text:
            ComandosO.apagado()

        else:
            chatBot(text)
            print("*" + name1 + " escuchando")
            text = recognition.recognize()
            if text is not None:
                comando.comando(text)

def chatBot(text):


    # Petición de respuesta a OpenAI GPT-3
    response = openai.Completion.create(
        engine="text-davinci-002",
        prompt= previous_context+text,
        max_tokens=1024,
        n=1,
        stop=None,
        temperature=0.5,
    )

    # Imprimir respuesta
    speech.talk(response["choices"][0]["text"])

class ComandosO:


    def ejecuta(text):
        speech.talk(no)

    def busca(text):
        bus = text.replace("busca" + "", "")
        print("*Realizando busquedad.")
        webbrowser.open("https://www.google.com/search?client=opera-gx&q=" + bus)
        speech.talk("Aqui estan los resultado de " + bus + " ," + usu)

    def hora():
        hora = datetime.datetime.now().strftime('%I:%M %p')
        speech.talk("Son las " + hora + ", " + usu)
        print("*Reloj: " + hora)

    def reproduce(text):
        music = text.replace("reproduce" + "", "")
        speech.talk("Reproduciendo ")
        pywhatkit.playonyt(music)

    # Desarrollo
    def pausa_volumen():
        speech.talk(no)

    # Desarrollo
    def subir_volumen():
        speech.talk(no)

    # Desarrollo
    def bajar_volumen():
        speech.talk(no)

    # Desarrollo
    def muestrame(text):
        muestra = text.replace("muestrame" + "", "")
        if "bonito" in muestra:
            speech.talk(no)

    def apagado():
        speech.talk("Apagando el ordenador")
        subprocess.run("shutdown -s")

    def cierre(text):
        text = text.replace("cierra" + "", "")
        c = wmi.WMI()
        text = text + ".exec"
        speech.talk("Buscando")
        for process in c.Win32_Process():
            print(process.ProcessId, process.Name)
            if process.Name in text:
                speech.talk("Ejecutando cerrado de " + text + "," + usu)
                print("*Cerrando", process.ProcessId, process.Name)
                os.kill(process.ProcessId, SIGTERM)
                return
        speech.talk("no logre encontrar " + text + " entre procesos")
