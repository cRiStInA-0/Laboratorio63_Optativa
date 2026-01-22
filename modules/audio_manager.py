import os
# Para acceder a variables de entorno de forma segura
import time
# Para pausas entre consultas en el polling
import requests
# Para hacer peticiones HTTP a la API AssemblyAI
import sounddevice as sd
# Para capturar audio desde el micrófono
from scipy.io.wavfile import write
# Para guardar el audio en formato WAV

# ============================================================
# CONFIGURACIÓN GLOBAL DE CONSTANTES
# ============================================================
API_KEY = os.getenv("AAI_API_KEY", "TU_API_KEY_AQUI")
# Obtiene la clave API desde la variable de entorno AAI_API_KEY
# Si no existe, usa valor por defecto "TU_API_KEY_AQUI"
# ⚠ En producción, nunca usar valores por defecto
UPLOAD_ENDPOINT = "https://api.assemblyai.com/v2/upload"
# URL del servidor AssemblyAI para subir archivos de audio
TRANSCRIBE_ENDPOINT = "https://api.assemblyai.com/v2/transcript"
# URL del servidor AssemblyAI para solicitar transcripciones
HEADERS = {
 "authorization": API_KEY,
 "content-type": "application/json"
}
# Cabeceras HTTP necesarias para todas las peticiones autenticadas
SAMPLERATE = 16000
# Frecuencia de muestreo estándar para reconocimiento de voz
# 16 kHz es estándar en industria de ASR (Automatic Speech Recognition)
DURATION_SECONDS = 5
# Duración de la grabación en segundos
WAV_FILENAME = "temp_audio.wav"
# Nombre temporal del archivo de audio (se borra después)


# ============================================================
# FUNCIÓN 1: GRABAR AUDIO
# ============================================================
def grabar_audio():

 print(" Grabando audio...")
 # Mensaje visual para el usuario

 # Captura muestras de audio PCM de 16 bits, mono canal
 audio = sd.rec(
    int(SAMPLERATE * DURATION_SECONDS), # Número de muestras (5 segundos)
    samplerate=SAMPLERATE, # Frecuencia: 16000 Hz
    channels=1, # Mono (1 canal)
    dtype='int16' # Tipo de dato: entero 16 bits
 )

 sd.wait()
 # Bloquea la ejecución hasta que finalice la grabación

 # Guarda el audio grabado en formato WAV
 write(WAV_FILENAME, SAMPLERATE, audio)

 print(f"✅ Audio grabado en '{WAV_FILENAME}'")
 # Confirmación de éxito

 return WAV_FILENAME


# ============================================================
# FUNCIÓN 2: SUBIR AUDIO A ASSEMBLYAI
# ============================================================
def subir_audio(filepath):

 print(" Subiendo archivo a AssemblyAI...")

 # Abre el archivo en modo lectura binaria ('rb')
 with open(filepath, 'rb') as f:
    # Realiza petición POST con el archivo
    response = requests.post(
        UPLOAD_ENDPOINT, # URL de subida
        headers={"authorization": API_KEY}, # Autenticación
        data=f # El archivo como cuerpo
    )

 # Verifica que la subida fue exitosa (código HTTP 200)
 if response.status_code == 200:
    # Extrae la URL del archivo subido del JSON de respuesta
    upload_url = response.json()["upload_url"]
    print(f" Archivo subido: {upload_url}")
    return upload_url
 else:
    # Si hay error, lanza excepción con detalles
    raise Exception(f" Error: {response.text}")


# ============================================================
# FUNCIÓN 3: SOLICITAR TRANSCRIPCIÓN
# ============================================================
def solicitar_transcripcion(audio_url):

 print(" Solicitando transcripción...")

 # Datos a enviar: URL del audio e idioma
 json_data = {
    "audio_url": audio_url, # URL del audio a transcribir
    "language_code": "es" # Configura idioma a español
 }

 # Realiza petición POST para solicitar transcripción
 response = requests.post(
    TRANSCRIBE_ENDPOINT, # URL de transcripción
    json=json_data, # Datos en formato JSON
    headers=HEADERS # Cabeceras con autenticación
 )

 # Verifica que la solicitud fue exitosa
 if response.status_code == 200:
    # Extrae el ID único de la transcripción
    transcript_id = response.json()["id"]
    print(f" ID de transcripción: {transcript_id}")
    return transcript_id
 else:
    # Si hay error, lanza excepción
    raise Exception(f" Error: {response.text}")


# ============================================================
# FUNCIÓN 4: POLLING - ESPERAR RESULTADO
# ============================================================
def obtener_resultado_transcripcion(transcript_id):

 print(" Esperando resultados...")

 # Construye URL para consultar estado de la transcripción
 polling_endpoint = f"{TRANSCRIBE_ENDPOINT}/{transcript_id}"

 # Bucle infinito hasta obtener resultado o error
 while True:
    # Hace petición GET para consultar estado
    response = requests.get(polling_endpoint, headers=HEADERS)

    # Extrae el estado actual de la transcripción
    status = response.json()["status"]

    if status == "completed":
        # Transcripción completa
        print(" Completada.")
        # Extrae y retorna el texto transcrito
        return response.json().get("text", "")

    elif status == "error":
        # Error en la transcripción
        error_msg = response.json()['error']
        raise Exception(f" {error_msg}")

    else:
        # Aún procesándose (estados: queued, processing)
        print(f" Estado: {status}. Reintentando en 2s...")
        time.sleep(2) # Pausa 2 segundos antes de consultar de nuevo


# ============================================================
# FUNCIÓN 5: ORQUESTADOR PRINCIPAL
# ============================================================
def escuchar():
 try:
    # Paso 1: Grabar
    archivo = grabar_audio()

    # Paso 2: Subir
    url_audio = subir_audio(archivo)

    # Paso 3: Solicitar transcripción
    id_transcripcion = solicitar_transcripcion(url_audio)

    # Paso 4: Esperar resultado con polling
    texto = obtener_resultado_transcripcion(id_transcripcion)

    # Paso 5: Retornar texto
    return texto

 except Exception as e:
    # Captura cualquier error y lo imprime
    print(f" Error: {e}")
    # Retorna cadena vacía para que la GUI sepa que algo falló
    return ""