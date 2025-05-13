from flask import Flask, request
import requests
import os
import json

app = Flask(__name__)

DISCORD_WEBHOOK_URL = os.environ.get("DISCORD_WEBHOOK_URL")

@app.route("/webhook", methods=["POST"])
def webhook():
    data = request.json
    print("Received data:", data)

    # Safely format data as a string
    try:
        block_data = data["event"]["data"]["block"]
        formatted_data = json.dumps(block_data, indent=2)[:1900]  # Discord limit is 2000 characters
    except (KeyError, TypeError) as e:
        print(f"Error extracting block data: {e}")
        # Fallback to sending the whole data if extraction fails
        formatted_data = json.dumps(data, indent=2)[:1900]

    message = {
        "content": f"🚨 New webhook received:\n```json\n{formatted_data}\n```"
    }

    if DISCORD_WEBHOOK_URL:
        response = requests.post(DISCORD_WEBHOOK_URL, json=message)
        print("Discord response status:", response.status_code)
        print("Discord response text:", response.text)
    else:
        print("DISCORD_WEBHOOK_URL not set!")

    return "", 200

@app.route("/", methods=["GET"])
def home():
    return "Flask webhook server is live!", 200

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(debug=True, host="0.0.0.0", port=port)
