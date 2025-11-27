from django.conf import settings
import requests


def send_to_telegram(name, email, phon_number, message):
  bot_token = settings.TELEGRAM_BOT_TOKEN
  chat_id = settings.TELEGRAM_CHAT_ID

  # Текст сообщения
  text = f"""
📞 Новая заявка с сайта!

Имя: {name}
Email: {email}
Телефон: {phon_number}
Сообщение: {message}
    """
    # Отправляем в Telegram
  url = f"https://api.telegram.org/bot{bot_token}/sendMessage"
  data = {
      'chat_id': chat_id,
      'text': text
  }
  try:
    requests.post(url, data=data)
    print('Уведомление отправлено в Telegram!')
  except:
    print('Ошибка отправки в телеграм')
