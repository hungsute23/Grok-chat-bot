from flask import Flask, request
import requests
import os

app = Flask(__name__)

# Use provided keys as fallback if environment variables are not set
TELEGRAM_BOT_TOKEN = os.getenv("TELEGRAM_BOT_TOKEN", "7638671660:AAG2fN5BmHTb7OoFtdmbQnWPR1Ct1w2OnDI")
GORK_API_KEY = os.getenv("GORK_API_KEY", "xai-YubXTPr9aEQ3rQuY77HCRxJOEii0oV2WSiNnnFFSXNvTmvIOUpCWuFOLlquJ2W6dSz49syoWdiA3TAa9")
TELEGRAM_API_URL = f"https://api.telegram.org/bot{TELEGRAM_BOT_TOKEN}"

@app.route('/webhook', methods=['POST'])
def webhook():
    data = request.json
    if "message" in data:
        chat_id = data["message"]["chat"]["id"]
        user_message = data["message"]["text"]

        # Call Gork API
        gork_response = requests.get(
            "https://api.gork.com/endpoint",  # Replace with actual endpoint
            headers={"Authorization": f"Bearer {GORK_API_KEY}"},
            params={"query": user_message}
        )
        gork_data = gork_response.json()

        # Send response back to Telegram
        response_message = gork_data.get("response", "Sorry, I couldn't process that.")
        requests.post(
            f"{TELEGRAM_API_URL}/sendMessage",
            json={"chat_id": chat_id, "text": response_message}
        )
    return "OK", 200

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=int(os.getenv("PORT", 5000)))
