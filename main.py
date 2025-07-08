import telebot
import requests

# Replace this with your actual Telegram Bot Token
TELEGRAM_TOKEN = '8161529372:AAFMce21KHTTrIfyn6AIvF6a1Pf7VeJqg1g'
bot = telebot.TeleBot(TELEGRAM_TOKEN)

def get_ai_reply(message):
    response = requests.post(
        "https://api.pawan.krd/v1/chat/completions",
        headers={
            "Authorization": "Bearer pk-anon-key",
            "Content-Type": "application/json"
        },
        json={
            "model": "pai-001",
            "messages": [
                {"role": "system", "content": "You are a friendly Telugu-English AI who helps users"},
                {"role": "user", "content": message}
            ]
        }
    )
    return response.json()["choices"][0]["message"]["content"]

@bot.message_handler(func=lambda message: True)
def handle_message(message):
    try:
        reply = get_ai_reply(message.text)
        bot.reply_to(message, reply)
    except Exception as e:
        bot.reply_to(message, "AI error: " + str(e))

print("✅ Bot is running...")
bot.polling()
