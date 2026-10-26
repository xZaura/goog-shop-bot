
import os
import requests
from flask import Flask, request

TOKEN = os.environ["BOT_TOKEN"]
API = f"https://api.telegram.org/bot{TOKEN}/"

app = Flask(__name__)


def send_message(chat_id, text):
    requests.post(API + "sendMessage", json={
        "chat_id": chat_id,
        "text": text
    }, timeout=10)


@app.route("/", methods=["GET"])
def home():
    return "Goog Shop Bot is running!"


@app.route("/webhook", methods=["POST"])
def webhook():
    data = request.get_json(silent=True) or {}
    message = data.get("message", {})
    chat = message.get("chat", {})
    chat_id = chat.get("id")
    text = message.get("text", "")

    if chat_id and text == "/start":
        send_message(
            chat_id,
            "Привет! Это Goog Shop.\n\n"
            "Для заказа напиши администратору магазина."
        )

    return {"ok": True}


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=int(os.environ.get("PORT", 8080)))
