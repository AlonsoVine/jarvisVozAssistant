import speech_recognition as sr
import pyttsx3
import os
import requests
import webbrowser
import platform
import smtplib
from datetime import datetime, timedelta
import time


def hablar(texto):
    """Función para convertir texto a voz"""
    engine = pyttsx3.init()
    engine.setProperty('rate', 150)  # Velocidad del habla
    engine.setProperty('volume', 0.9)  # Volumen de la voz
    engine.say(texto)
    engine.runAndWait()


def escuchar_comando():
    """Función para escuchar y reconocer comandos de voz"""
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        print("Escuchando...")
        recognizer.adjust_for_ambient_noise(source)
        try:
            audio = recognizer.listen(source, timeout=5)
        except sr.WaitTimeoutError:
            print("No se detectó ningún audio a tiempo.")
            return None
    try:
        comando = recognizer.recognize_google(audio, language="es-ES")
        print(f"Has dicho: {comando}")
        return comando.lower()
    except sr.UnknownValueError:
        print("No pude entender el audio.")
        return None
    except sr.RequestError as e:
        print(f"Error al conectarse con el servicio de reconocimiento de voz; {e}")
        return None


def abrir_aplicacion(nombre):
    """Función para abrir aplicaciones dependiendo del sistema operativo"""
    sistema = platform.system()
    try:
        if "navegador" in nombre:
            hablar("Abriendo el navegador")
            if sistema == "Windows":
                os.system("start chrome")
            elif sistema == "Darwin":  # macOS
                os.system("open -a Safari")
            else:  # Linux
                os.system("google-chrome")
        elif "calculadora" in nombre:
            hablar("Abriendo la calculadora")
            if sistema == "Windows":
                os.system("calc")
            elif sistema == "Darwin":  # macOS
                os.system("open -a Calculator")
            else:  # Linux
                os.system("gnome-calculator")
        else:
            hablar(f"No sé cómo abrir {nombre}")
    except Exception as e:
        hablar(f"Lo siento, hubo un error al abrir la aplicación: {e}")


def buscar_en_internet(consulta):
    """Función para realizar una búsqueda en Google"""
    url = f"https://www.google.com/search?q={consulta}"
    try:
        webbrowser.open(url)
        hablar(f"Buscando {consulta} en Google")
    except Exception as e:
        hablar(f"Lo siento, no pude realizar la búsqueda debido a: {e}")


def obtener_clima(ciudad):
    """Función para consultar el clima de una ciudad usando la API de OpenWeatherMap"""
    api_key = "TU_API_KEY_DE_OPENWEATHERMAP"
    url = f"http://api.openweathermap.org/data/2.5/weather?q={ciudad}&appid={api_key}&lang=es&units=metric"
    try:
        response = requests.get(url)
        data = response.json()
        if data["cod"] == 200:
            temp = data["main"]["temp"]
            descripcion = data["weather"][0]["description"]
            hablar(f"El clima en {ciudad} es {descripcion} con una temperatura de {temp} grados Celsius.")
        else:
            hablar(f"No pude obtener el clima para {ciudad}.")
    except requests.exceptions.RequestException as e:
        hablar(f"Error al conectarse a la API del clima: {e}")


def crear_recordatorio(mensaje, minutos):
    """Función para crear un recordatorio que avise después de X minutos"""
    hablar(f"Recordatorio configurado: {mensaje} en {minutos} minutos.")
    time.sleep(minutos * 60)  # Convertir minutos a segundos
    hablar(f"Recordatorio: {mensaje}")


def enviar_correo(destinatario, asunto, mensaje):
    """Función para enviar un correo electrónico (requiere configuración previa del servidor de correo)"""
    try:
        servidor = smtplib.SMTP('smtp.gmail.com', 587)
        servidor.starttls()
        servidor.login("TUCORREO@gmail.com", "TUPASSWORD")
        correo = f"Subject: {asunto}\n\n{mensaje}"
        servidor.sendmail("TUCORREO@gmail.com", destinatario, correo)
        servidor.quit()
        hablar("Correo enviado correctamente.")
    except Exception as e:
        hablar(f"Lo siento, no pude enviar el correo debido a: {e}")


def ejecutar_asistente():
    """Función principal para ejecutar el asistente virtual"""
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
            elif "recordatorio" in comando:
                try:
                    partes = comando.split("en")
                    mensaje = partes[0].replace("recordatorio", "").strip()
                    minutos = int(partes[1].strip().split()[0])
                    crear_recordatorio(mensaje, minutos)
                except ValueError:
                    hablar("No entendí la cantidad de minutos. Por favor, repite el comando.")
            elif "enviar correo" in comando:
                hablar("¿A quién quieres enviar el correo?")
                destinatario = escuchar_comando()
                hablar("¿Cuál es el asunto del correo?")
                asunto = escuchar_comando()
                hablar("¿Cuál es el mensaje del correo?")
                mensaje = escuchar_comando()
                enviar_correo(destinatario, asunto, mensaje)
            elif "salir" in comando or "adiós" in comando:
                hablar("Adiós. Que tengas un buen día.")
                break
            else:
                hablar("Lo siento, no entendí ese comando.")
        else:
            hablar("Lo siento, no pude entenderte. Intenta de nuevo.")

