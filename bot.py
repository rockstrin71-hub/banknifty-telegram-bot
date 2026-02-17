import requests
import time

BOT_TOKEN = "8447975135:AAGN4QPvD8M2jcuzSckmo3qt__D5NmjUEbQ"
CHAT_ID = "1271354519"

def send_telegram_message(message):
    url = f"https://api.telegram.org/bot{BOT_TOKEN}/sendMessage"
    payload = {
        "chat_id": CHAT_ID,
        "text": message
    }
    requests.post(url, data=payload)

# BankNifty price function (IMPORTANT – loop se pehle)
def get_banknifty_price():
    url = "https://query1.finance.yahoo.com/v7/finance/quote?symbols=%5ENSEBANK"
    data = requests.get(url).json()
    price = data['quoteResponse']['result'][0]['regularMarketPrice']
    return price

send_telegram_message("Bot started and tracking BankNifty 📈")

while True:
    price = get_banknifty_price()
    send_telegram_message(f"BankNifty Live Price: {price}")
    time.sleep(600)
