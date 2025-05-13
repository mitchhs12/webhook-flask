from flask import Flask, request
import requests
import os

app = Flask(__name__)

DISCORD_WEBHOOK_URL = os.environ.get("DISCORD_WEBHOOK_URL")  # Add this in Render environment variables

@app.route("/webhook", methods=["POST"])
def webhook():
    data = request.json
    print("Received data:", data)

    # Format the message for Discord
    message = {
        "content": f"🚨 New webhook received:\n```{data}```"
    }

    # Forward to Discord
    if DISCORD_WEBHOOK_URL:
        requests.post(DISCORD_WEBHOOK_URL, json=message)

    return "", 200

if __name__ == "__main__":
    app.run(debug=True)
