# Laboratorio: Semáforo Tricolor Controlado por Voz con AssemblyAI
## Descripción
Aplicación de control remoto de un panel de control mediante reconocimiento de voz en tiempo real usando AssemblyAI como motor de transcripción cloud.

## Objetivo Educativo
Desarrollar una aplicación modular en Python que simule el panel de control de un robot industrial 4.0, capaz de responder a comandos de voz mediante AssemblyAI asíncrono y mostrar el estado de sus sensores en una interfaz visual creada con Tkinter.

El objetivo es comprender cómo se integran tecnologías de voz con la nube, visualización de datos y automatización en entornos industriales inteligentes

## Comandos Disponibles
- "activar robot" → Enciende los sensores
- "detener robot" → Apaga los sensores
- "temperatura alta" → El sensor de temperatura se pone en rojo intenso y aparece un mensaje de alerta
- "revisar sensores" → Apaga todas las luces
- "salir" → Cierra la aplicación

## Instalación
1. Instalar dependencias:
 pip install -r requirements.txt
2. Configurar API key:
 $env:AAI_API_KEY="tu_clave_api"
3. Ejecutar la aplicación:
 python main.py

## Requisitos
- Python 3.8+
- Micrófono funcional
- Conexión a internet (para AssemblyAI)
- Cuenta en Assem