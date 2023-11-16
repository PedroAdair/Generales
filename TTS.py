from gtts import gTTS

def TextToSpeech(text:str, lang:str):
    tts = gTTS(text, lang = lang)
    tts.save('respuesta.mp3')
    print("mp3 hecho")

hola = "Buenos dias Alfonzo"
esp = 'es'


hello = "Good morning Alfonzo"
eng = 'en'

ola = "bom dia Afonzo"
por = 'pt'

TextToSpeech(text= "Hoy es un dia soleado", lang= 'es')