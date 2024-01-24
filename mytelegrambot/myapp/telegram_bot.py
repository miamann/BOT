from googletrans import Translator
import requests

API_link = "https://api.telegram.org/bot6798434569:AAF9WD4az7DJ7dPMZ8bNOcLNACb7jnCOg9k"

def run_telegram_bot():
    updates = requests.get(API_link + "/getUpdates?offset=-1").json()

    if "result" in updates and updates["result"]:
        for update in updates["result"]:
            chat_id = update["message"]["chat"]["id"]
            text = update["message"]["text"]

            if text.startswith('/translate_ru_en '):
                text_to_translate = text[len('/translate_ru_en '):]
                translator_to_en = Translator()
                translated_text_to_en = translator_to_en.translate(text_to_translate, dest='en').text
                response_text = f"Перевод на английский: {translated_text_to_en}"
                sent_message = requests.get(API_link + f"/sendMessage?chat_id={chat_id}&text={response_text}")

            elif text.startswith('/translate_en_ru '):
                text_to_translate = text[len('/translate_en_ru '):]
                translator_to_ru = Translator()
                translated_text_to_ru = translator_to_ru.translate(text_to_translate, dest='ru').text
                response_text = f"Перевод на русский: {translated_text_to_ru}"
                sent_message = requests.get(API_link + f"/sendMessage?chat_id={chat_id}&text={response_text}")

            elif text == '/help':
                response_text = (
                    "/translate_ru_en [текст] - перевести текст с русского на английский\n"
                    "/translate_en_ru [текст] - перевести текст с английского на русский\n"
                    "/help - справка\n"
                    "/about - информация о боте"
                )
                sent_message = requests.get(API_link + f"/sendMessage?chat_id={chat_id}&text={response_text}")

            elif text == '/about':
                response_text = "Привет! Я бот для перевода текста в Telegram. Приятно познакомиться!"
                sent_message = requests.get(API_link + f"/sendMessage?chat_id={chat_id}&text={response_text}")

            else:
                response_text = "Привет, для работы со мной ты можешь использовать команду /translate_ru_en, /translate_en_ru, /help или /about"
                sent_message = requests.get(API_link + f"/sendMessage?chat_id={chat_id}&text={response_text}")
    else:
        print("Нет обновления или пустой результат")

run_telegram_bot()
