# Asistente Virtual con Reconocimiento de Voz
![IMG](jarvis_readme.png "imagen header")

Este es un proyecto de **asistente virtual** desarrollado en Python, que permite realizar varias tareas mediante **comandos de voz**. El asistente puede realizar acciones como abrir aplicaciones, buscar en internet, consultar el clima, crear recordatorios, y enviar correos electrónicos, entre otros.

## Funcionalidades

1. **Reconocimiento de voz**: Captura comandos de voz usando el micrófono y los convierte en texto.
2. **Text-to-Speech**: Responde con voz a los comandos del usuario.
3. **Abrir aplicaciones**: Puedes abrir el navegador, calculadora, entre otras, dependiendo del sistema operativo.
4. **Búsqueda en Google**: Realiza una búsqueda en Google según el comando de voz.
5. **Consulta de clima**: Consulta el clima de una ciudad utilizando la API de OpenWeatherMap.
6. **Recordatorios**: Configura recordatorios para alertarte después de un tiempo especificado.
7. **Enviar correos**: Envía correos electrónicos de manera automática tras recibir comandos.

## Tecnologías Utilizadas

- Python 3
- [SpeechRecognition](https://pypi.org/project/SpeechRecognition/) para el reconocimiento de voz.
- [PyAudio](https://pypi.org/project/PyAudio/) para la captura de audio.
- [pyttsx3](https://pypi.org/project/pyttsx3/) para la síntesis de voz (Text-to-Speech).
- [requests](https://pypi.org/project/requests/) para consultar APIs (por ejemplo, clima).
- [smtplib](https://docs.python.org/3/library/smtplib.html) para enviar correos electrónicos.
- [webbrowser](https://docs.python.org/3/library/webbrowser.html) para realizar búsquedas en internet.

## Requisitos Previos

Antes de ejecutar este proyecto, asegúrate de tener instalados los siguientes componentes:

1. **Python 3.x**: Puedes descargarlo desde [python.org](https://www.python.org/downloads/).
2. **Librerías de Python**: Debes instalar las siguientes librerías usando `pip`:

   ```bash
   pip install SpeechRecognition PyAudio pyttsx3 requests
   ```
