import pyttsx3

usu="seicros"
no="Funcion en desarrollo"
name = "limbo"
name1="L1MB0"

#Talk
class SpeechModule:

    def __init__(self, voice=0, volume=7, rate=125):

        self.engine = pyttsx3.init()
        self.engine.setProperty("rate", rate)
        self.engine.setProperty("volume", volume)

        voices = self.engine.getProperty("voices")
        self.engine.setProperty("voice", voices[voice].id)

    def talk(self, text):

        print("*" + name1 + "...")

        self.engine.say(text)
        self.engine.runAndWait()
        print("'" + text + "'")