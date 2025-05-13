from flask import Flask, request
import requests
import os

app = Flask(__name__)

DISCORD_WEBHOOK_URL = os.environ.get("DISCORD_WEBHOOK_URL")

@app.route("/webhook", methods=["POST"])
def webhook():
    data = request.json
    print("Received data:", data)

    message = {
        "content": f"🚨 New webhook received:\n```{data}```"
    }

    if DISCORD_WEBHOOK_URL:
        requests.post(DISCORD_WEBHOOK_URL, json=message)

    return "", 200

@app.route("/", methods=["GET"])
def home():
    return "Flask webhook server is live!", 200

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(debug=True, host="0.0.0.0", port=port)
