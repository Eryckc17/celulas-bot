import telegram
import asyncio
import schedule
import time
import os
import random
from flask import Flask
from threading import Thread
from datetime import datetime

TOKEN = '8762017311:AAG5_BcZJeCLcQYKGsfbRg53_gXjuwSPltI'
CHAT_ID = '644581238'
bot = telegram.Bot(token=TOKEN)

app = Flask(__name__)

# Imágenes curadas (puedes cambiarlas luego)
IMG_ADULTOS = ["https://images.unsplash.com/photo-1504052434569-70ad5836ab65", "https://images.unsplash.com/photo-1542816417-0983c9c9ad53"]
IMG_JOVENES = ["https://images.unsplash.com/photo-1511632765486-a01980e01a18", "https://images.unsplash.com/photo-1517486808906-6c8b3f37a70f"]

# Amplia lista de mensajes por día y categoría
def get_message(day, is_joven):
    # Diccionario de mensajes según el día
    if day == 'tuesday': # Martes de Fe y Milagros
        return "¡Hoy es Martes de Fe y Milagros! Expectantes por lo que Dios hará en el culto. 🙏✨" if not is_joven else "¡Martes de poder! Prepárate para ver milagros en el culto hoy. ¡No faltes! ⚡🚀"
    elif day == 'wednesday': # Miércoles de Célula
        return "¡Miércoles de Célula! Es tiempo de compartir en unidad. 'Donde hay dos o tres congregados...' 📖🙌" if not is_joven else "¡Muchachos, hoy es célula! ¡A recargar pilas con la Palabra! 🔥😎"
    elif day == 'saturday': # Arena Joven
        return "¡Feliz sábado de servicio y comunión! 🌟" if not is_joven else "¡Hoy es Arena Joven! Fuego, visión y propósito. ¡Nos vemos allá! 💥🔥"
    elif day == 'sunday': # Culto Familiar
        return "¡Feliz domingo! Nos vemos en el Culto Familiar para honrar al Señor. ⛪🙌" if not is_joven else "¡Culto de familia hoy! Identidad y propósito. ¡Te esperamos! 🚀✨"
    else: # Días de aliento
        mensajes_a = ["¡Bendecido día! 'Encomienda al Señor tu camino' (Salmo 37:5). 🛡️", "¡La fidelidad de Dios es nueva cada mañana! ✨", "¡Sigamos adelante con la mirada puesta en Dios! 📖"]
        mensajes_j = ["¡Dale con todo hoy! Dios tiene un plan grande para tu vida. 🌟", "¡Muchachos, levántense con autoridad! ⚡", "¡No se detengan, el propósito de Dios es mayor! 🚀"]
        return random.choice(mensajes_a) if not is_joven else random.choice(mensajes_j)

async def enviar_bloque(hora):
    day = datetime.now().strftime('%A').lower()
    
    # 1. Adultos
    await bot.send_photo(chat_id=CHAT_ID, photo=random.choice(IMG_ADULTOS), caption=f"🟢 *MENSAJE {hora} - FAMILIA*\n\n{get_message(day, False)}", parse_mode='Markdown')
    
    # 2. Jóvenes con Trivia
    trivias = [("¿Quién fue el hombre más fuerte?", "Sansón"), ("¿Quién fue tragado por un pez?", "Jonás"), ("¿Cuál es el libro más corto?", "2 Juan"), ("¿Quién construyó el Arca?", "Noé"), ("¿Quién fue vendido por sus hermanos?", "José")]
    q, a = random.choice(trivias)
    msg_j = f"🔥 *IGNITE - {hora}*\n\n{get_message(day, True)}\n\n💡 *Trivia:* {q}\n*Respuesta:* ||{a}||"
    await bot.send_photo(chat_id=CHAT_ID, photo=random.choice(IMG_JOVENES), caption=msg_j, parse_mode='Markdown')

def run_scheduler():
    # Programación
    schedule.every().day.at("08:00").do(lambda: asyncio.run(enviar_bloque("08:00 AM")))
    schedule.every().day.at("13:00").do(lambda: asyncio.run(enviar_bloque("01:00 PM")))
    schedule.every().day.at("20:00").do(lambda: asyncio.run(enviar_bloque("08:00 PM")))
    while True:
        schedule.run_pending()
        time.sleep(60)

if __name__ == '__main__':
    Thread(target=run_scheduler).start()
    app.run(host='0.0.0.0', port=int(os.environ.get('PORT', 8080)))
