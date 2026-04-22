import telegram
import asyncio
import schedule
import time
import os
from flask import Flask
from threading import Thread
from datetime import datetime

TOKEN = '8762017311:AAG5_BcZJeCLcQYKGsfbRg53_gXjuwSPltI'
CHAT_ID = '644581238'
bot = telegram.Bot(token=TOKEN)

app = Flask(__name__)
@app.route('/')
def home():
    return "Bot de mensajes activo"

def get_messages():
    day = datetime.now().strftime('%A').lower()
    
    # Mensajes personalizados con Emojis
    if day == 'wednesday': # Miércoles
        adultos = "🟢 *MENSAJE CÉLULAS:* \n\n¡Hola familia! 👋 Hoy es nuestro miércoles de célula. Un tiempo especial para crecer juntos. Recuerden: *'¡Qué bueno y qué agradable es cuando los hermanos conviven en armonía!'* (Salmo 133:1). ¡Los espero hoy con expectativas! 🙌✨"
        joven = "🔥 *MENSAJE JUVENIL:* \n\n¡Ey, equipo! 🚀 ¡Hoy es día de célula! Es el momento perfecto para conectar, reír y recargar pilas con amigos. *'Considerémonos unos a otros para estimularnos al amor y a las buenas obras'* (Hebreos 10:24). ¡Va a estar brutal, no faltes! ⚡💪"
    elif day == 'tuesday': # Martes
        adultos = "🟢 *MENSAJE:* \n\n¡Feliz martes de Fe y Milagros! 🙏✨ Vayamos expectantes por lo que Dios hará hoy. *'Solo en Dios halla descanso mi alma'* (Salmo 62:5). ¡Nos vemos en el culto! ⛪🔥"
        joven = "🔥 *MENSAJE JUVENIL:* \n\n¡Martes de milagros! ⚡ No te muevas por miedo, muévete por fe. *'Porque no nos ha dado Dios un espíritu de cobardía, sino de poder'* (2 Timoteo 1:7). ¡Sé audaz hoy! 😎🙌"
    elif day == 'saturday': # Sábado
        adultos = "🟢 *MENSAJE:* \n\n¡Feliz sábado! ☀️ Un día para servir y amar al prójimo. Que Su luz brille a través de cada uno de nosotros hoy. 🤝❤️"
        joven = "🚀 *ARENA JOVEN:* \n\n¡Fuego, visión y pasión! 🔥 Hoy es *Ignite* a las 5:00 PM. ¡Prepárate para lo que Dios quiere encender en ti! ⚡💣 ¡Te esperamos!"
    elif day == 'sunday': # Domingo
        adultos = "🟢 *CULTO FAMILIAR:* \n\n¡Feliz domingo! 👨‍👩‍👧‍👦 Nos vemos a las 10:00 AM para honrar al Señor en unidad. *'Yo y mi casa serviremos al Señor'* (Josué 24:15). ¡Bendiciones! 🙌⛪"
        joven = "🔥 *DOMINGO:* \n\n¡Hoy culto de familia! ⛪ Identidad, honra y propósito. ¡No te pierdas lo que Dios tiene para los jóvenes hoy! 🚀🙌✨"
    else: # Días libres
        adultos = "🟢 *MENSAJE:* \n\n¡Bendecido día! 🌟 Que Su paz, que sobrepasa todo entendimiento, guarde hoy sus corazones. (Filipenses 4:7). ¡Ánimo en todo lo que emprendas! 🌿💪"
        joven = "🔥 *MENSAJE:* \n\n¡Vamos a darle con todo hoy! ⚡ Dios tiene un plan grande para tu vida. *'Porque yo sé muy bien los planes que tengo para ustedes'* (Jeremías 29:11). ¡A brillar! 😎🚀💫"
        
    return adultos, joven

async def enviar_mensajes():
    msg_a, msg_j = get_messages()
    await bot.send_message(chat_id=CHAT_ID, text=msg_a, parse_mode='Markdown')
    await bot.send_message(chat_id=CHAT_ID, text=msg_j, parse_mode='Markdown')

def run_scheduler():
    # Mensaje de prueba inmediato al arrancar
    asyncio.run(enviar_mensajes())
    
    # Programación diaria
    schedule.every().day.at("08:00").do(lambda: asyncio.run(enviar_mensajes()))
    schedule.every().day.at("15:00").do(lambda: asyncio.run(enviar_mensajes()))
    
    while True:
        schedule.run_pending()
        time.sleep(60)

if __name__ == '__main__':
    Thread(target=run_scheduler).start()
    app.run(host='0.0.0.0', port=int(os.environ.get('PORT', 8080)))
