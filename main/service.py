from django.conf import settings
import requests


def send_to_telegram(user_data) -> str:
  bot_token = settings.TELEGRAM_BOT_TOKEN
  chat_id = settings.TELEGRAM_CHAT_ID

  # Текст сообщения
  text = f"""
📞 Новая заявка с сайта!

Имя: {user_data['name']}
Email: {user_data['email']}
Телефон: {user_data['phon_number']}
Сообщение: {user_data['message']}
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
