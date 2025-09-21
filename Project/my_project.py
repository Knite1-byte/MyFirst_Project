import telebot
import requests
import os
from dotenv import load_dotenv

load_dotenv()  # загружает переменные из .env

# Настройки
TELEGRAM_TOKEN = os.getenv('TELEGRAM_TOKEN')

# Инициализация бота
bot = telebot.TeleBot(TELEGRAM_TOKEN)

def get_random_fact():
    """Получает случайный факт с другого API."""
    try:
        # Используем другое бесплатное API
        response = requests.get('https://uselessfacts.jsph.pl/random.json?language=en')
        data = response.json()
        # Важно: здесь ключ для текста другой, не 'text', а 'text'
        return data['text']
    except Exception as e:
        print(e)
        return "Не смог получить факт :( Попробуй еще раз!"

# --- ОБРАБОТЧИКИ КОМАНД ---
@bot.message_handler(commands=['start'])
def send_welcome(message):
    """Отвечает на команду /start."""
    welcome_text = (
        "Привет! 👋 Я бот, который знает много случайных фактов.\n"
        "Просто отправь мне команду /fact, и я пришлю тебе что-нибудь интересное!"
    )
    bot.reply_to(message, welcome_text)

@bot.message_handler(commands=['fact'])
def send_fact(message):
    """Отвечает на команду /fact, отправляя случайный факт."""
    fact = get_random_fact()
    bot.reply_to(message, fact)

# --- ЗАПУСК БОТА ---
print("Бот запущен!")
bot.polling(none_stop=True)

