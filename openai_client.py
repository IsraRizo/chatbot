import os
from openai import OpenAI
from dotenv import load_dotenv

# Cargar variables de entorno desde .env
load_dotenv()
print(os.getenv("OPENAI_API_KEY"))
# Leer la API Key
api_key = os.getenv("OPENAI_API_KEY")
print(api_key)

# Inicializar cliente
client = OpenAI(api_key=api_key)

# Lista global para guardar el historial de mensajes
message_history = [
    {"role": "system", "content": "You are a helpful assistant."}
]

# Función para consultar OpenAI
def chat_openai(question: str) -> str:
    try:
        # Agregar la pregunta del usuario al historial
        message_history.append({"role": "user", "content": question})

        response = client.chat.completions.create(
            model="gpt-4o-mini",  # Cambia a gpt-4 si quieres
            messages=message_history,
            max_tokens=300
        )

         # Obtener respuesta del asistente
        assistant_reply = response.choices[0].message.content.strip()

        # Agregar respuesta del asistente al historial
        message_history.append({"role": "assistant", "content": assistant_reply})

        return assistant_reply
    except Exception as e:
        return f"Error: {e}"
