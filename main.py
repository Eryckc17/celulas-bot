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
    
    # Lógica de mensajes según el día
    if day == 'wednesday': # Miércoles
        adultos = "🟢 *MENSAJE CÉLULAS:* ¡Hola familia! Hoy es miércoles de célula. Recordemos: '¡Qué bueno y qué agradable es cuando los hermanos conviven en armonía!' (Salmo 133:1). ¡Los espero hoy!"
        joven = "🔥 *MENSAJE JUVENIL:* ¡Equipo! Hoy es día de célula, nuestro momento de conectar y recargar pilas. 'Considerémonos unos a otros para estimularnos al amor y a las buenas obras' (Hebreos 10:24). ¡No faltes!"
    elif day == 'tuesday': # Martes
        adultos = "🟢 *MENSAJE:* ¡Hoy es martes de Fe y Milagros! Expectantes por lo que Dios hará. (Salmo 62:5)."
        joven = "🔥 *MENSAJE JUVENIL:* ¡Martes de milagros! Vayamos con audacia. (2 Timoteo 1:7)."
    elif day == 'saturday': # Sábado
        adultos = "🟢 *MENSAJE:* ¡Sábado de servicio y amor al prójimo!"
        joven = "🚀 *ARENA JOVEN:* ¡Hoy es Ignite! Fuego, visión y pasión a las 5:00 PM. ¡Te esperamos!"
    elif day == 'sunday': # Domingo
        adultos = "🟢 *CULTO FAMILIAR:* Hoy domingo a las 10:00 AM, unidad y amor en casa. (Josué 24:15)."
        joven = "🔥 *DOMINGO:* ¡Hoy culto de familia! Identidad y honra. ¡Nos vemos!"
    else: # Días libres
        adultos = "🟢 *MENSAJE:* ¡Feliz día! Que la paz de Dios guarde sus corazones. (Filipenses 4:7)."
        joven = "🔥 *MENSAJE:* ¡A darle con todo hoy! Dios tiene algo grande para tu vida. (Jeremías 29:11)."
        
    return adultos, joven

async def enviar_mensajes():
    msg_a, msg_j = get_messages()
    await bot.send_message(chat_id=CHAT_ID, text=msg_a, parse_mode='Markdown')
    await bot.send_message(chat_id=CHAT_ID, text=msg_j, parse_mode='Markdown')

def run_scheduler():
    # Enviar mensaje inmediato de prueba
    asyncio.run(enviar_mensajes())
    
    # Programar envíos
    schedule.every().day.at("08:00").do(lambda: asyncio.run(enviar_mensajes()))
    schedule.every().day.at("15:00").do(lambda: asyncio.run(enviar_mensajes()))
    
    while True:
        schedule.run_pending()
        time.sleep(60)

if __name__ == '__main__':
    Thread(target=run_scheduler).start()
    app.run(host='0.0.0.0', port=int(os.environ.get('PORT', 8080)))
