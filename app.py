import os
from flask import Flask
from dotenv import load_dotenv
from twilio.rest import Client
from twilio.twiml.messaging_response import MessagingResponse # for handling of webhooks

load_dotenv(verbose=True)
account_sid = os.getenv('TWILIO_ACCOUNT_SID')
auth_token = os.getenv('TWILIO_AUTH_TOKEN')
twilio_sandbox_phone=os.getenv('TWILIO_SANDBOX_PHONE') # pre approved twilio sandbox phone
incoming_phone = os.getenv('WHATSAPP_INCOMING_PHONE') # my phone number
client = Client(account_sid, auth_token)

app = Flask(__name__)

@app.route("/")
def hello():
    message = client.messages.create(
        body="Hello there!",
        from_=twilio_sandbox_phone,
        to=incoming_phone,
    )
    print(message.sid)
    return "Hello world"

# webhook url - need to set up on twilio console
@app.route("/message", methods=['POST'])
def whats_app_reply():
    resp = MessagingResponse()
    resp.message("obrigado")
    return str(resp)

if __name__ == '__main__':
    app.run()
