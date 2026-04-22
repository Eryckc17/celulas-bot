import telegram
import asyncio
import schedule
import time
import os
from flask import Flask
from threading import Thread

# Tus datos
TOKEN = '8762017311:AAG5_BcZJeCLcQYKGsfbRg53_gXjuwSPltI'
CHAT_ID = '644581238'
bot = telegram.Bot(token=TOKEN)

app = Flask(__name__)
@app.route('/')
def home():
    return "Bot activo y funcionando"

async def enviar_mensajes(es_prueba=False):
    if es_prueba:
        mensaje_adultos = "✅ *BOT ACTIVADO:* Iniciando sistema de mensajes automáticos."
        mensaje_joven = "🚀 *BOT ACTIVADO:* Sistema joven listo."
    else:
        mensaje_adultos = "🟢 *MENSAJE CÉLULAS:* (Tu mensaje para hoy aquí)"
        mensaje_joven = "🔥 *MENSAJE JUVENIL:* (Tu mensaje para hoy aquí)"
    
    await bot.send_message(chat_id=CHAT_ID, text=mensaje_adultos, parse_mode='Markdown')
    await bot.send_message(chat_id=CHAT_ID, text=mensaje_joven, parse_mode='Markdown')

def run_scheduler():
    # Mensaje de prueba inmediato al arrancar
    asyncio.run(enviar_mensajes(es_prueba=True))
    
    # Programación diaria
    schedule.every().day.at("08:00").do(lambda: asyncio.run(enviar_mensajes()))
    schedule.every().day.at("15:00").do(lambda: asyncio.run(enviar_mensajes()))
    
    while True:
        schedule.run_pending()
        time.sleep(60)

if __name__ == '__main__':
    Thread(target=run_scheduler).start()
    app.run(host='0.0.0.0', port=int(os.environ.get('PORT', 8080)))
