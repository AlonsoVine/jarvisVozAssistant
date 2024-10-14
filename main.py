import speech_recognition as sr
import pyttsx3
import os
import requests
import webbrowser

def hablar(texto):
    engine = pyttsx3.init()
    engine.setProperty('rate', 150)
    engine.setProperty('volume', 0.9)
    engine.say(texto)
    engine.runAndWait()

def escuchar_comando():
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        print("Escuchando...")
        recognizer.adjust_for_ambient_noise(source)
        audio = recognizer.listen(source)
    try:
        comando = recognizer.recognize_google(audio, language="es-ES")
        print(f"Has dicho: {comando}")
        return comando.lower()
    except sr.UnknownValueError:
        print("No pude entender el audio.")
        return None
    except sr.RequestError:
        print("Error al conectarse con el servicio de reconocimiento de voz.")
        return None

def abrir_aplicacion(nombre):
    if "navegador" in nombre:
        hablar("Abriendo el navegador")
        os.system("start chrome")
    elif "calculadora" in nombre:
        hablar("Abriendo la calculadora")
        os.system("calc")
    else:
        hablar(f"No sé cómo abrir {nombre}")

def buscar_en_internet(consulta):
    url = f"https://www.google.com/search?q={consulta}"
    webbrowser.open(url)
    hablar(f"Buscando {consulta} en Google")

def obtener_clima(ciudad):
    api_key = "TU_API_KEY_DE_OPENWEATHERMAP"
    url = f"http://api.openweathermap.org/data/2.5/weather?q={ciudad}&appid={api_key}&lang=es&units=metric"
    response = requests.get(url)
    data = response.json()
    if data["cod"] == 200:
        temp = data["main"]["temp"]
        descripcion = data["weather"][0]["description"]
        hablar(f"El clima en {ciudad} es {descripcion} con una temperatura de {temp} grados Celsius.")
    else:
        hablar(f"No pude obtener el clima para {ciudad}.")

def ejecutar_asistente():
    hablar("Hola, soy tu asistente virtual. ¿En qué te puedo ayudar?")
    while True:
        comando = escuchar_comando()
        if comando:
            if "abrir" in comando:
                abrir_aplicacion(comando)
            elif "buscar" in comando:
                buscar_en_internet(comando.replace("buscar", "").strip())
            elif "clima" in comando:
                ciudad = comando.replace("clima", "").strip()
                obtener_clima(ciudad)
            elif "salir" in comando or "adiós" in comando:
                hablar("Adiós. Que tengas un buen día
