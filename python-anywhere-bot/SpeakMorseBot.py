from flask import Flask, request
import requests

from encrypt import encrypt
from decrypt import decrypt


app = Flask(__name__)


@app.route("/decrypt", methods=["GET"])
def decrypt_message():
    return {"decrypted_message": decrypt("/decrypt batata")}


@app.route("/post_new_morse", methods=["POST"])
def new_message():
    body = request.json
    app.logger.info(f"You have a new message: {body}")
    answer, id = construct_answer(body)
    send_message(answer, id)

    return {"ok": True, "resp": answer}

def construct_answer(body):
    message = body.get("message") or body.get("edited_message")
    username = message.get("from", {}).get("first_name", "Citizen")
    id = message.get("chat", {}).get("id")
    text_message = message.get("text")

    if not message or not text_message:
        return ("Sorry, I can only interpret text messages at the moment", id)

    if text_message == "/start":
        return ("Hi, my name is SpeakMorse Bot! I'm here to help you with speaking Morse. You can choose between encryption (/encrypt) and decryption (/decrypt) depending on your needs :) Have fun!", id)

    if text_message.split(" ")[0] == "/decrypt":
        app.logger.info(f"received message: {message}")

        return (decrypt(text_message), id)

    elif text_message.split(" ")[0] == "/encrypt":
        app.logger.info(f"received message: {text_message}")

        return (encrypt(text_message), id)

    return (f"Cheers, {username}! In order to help you with Morse coding, I need you to choose between my /encrypt or /decrypt methods. Shall we give it a try?", id)

def send_message(texto, id):
    endpoint = f"https://api.telegram.org/bot{BOT_TOKEN}/sendMessage"
    params = {
        "chat_id": id,
        "text": texto,
    }
    requests.get(endpoint, params)
