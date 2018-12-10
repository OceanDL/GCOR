# import all the libraries we will be using
from twilio.twiml.messaging_response import MessagingResponse

from odst.parse import Parser
from odst.rst import *
from flask import Flask, request
from twilio import twiml

# set up Flask to connect this code to the local host, which will
# later be connected to the internet through Ngrok
app = Flask(__name__)


# Main method. When a POST request is sent to our local host through Ngrok
# (which creates a tunnel to the web), this code will run. The Twilio service # sends the POST request - we will set this up on the Twilio website. So when # a message is sent over SMS to our Twilio number, this code will run
@app.route('/', methods=['POST'])
def sms():
    # Get the text in the message sent
    message_body = request.form['Body']
    resp = MessagingResponse()

    # Send the message body to the getReply message, where
    # we will query the String and formulate a response

    reply = getReply(message_body)

    # Text back our response!
    resp.message(reply)
    return str(resp)


def getReply(message):
    p = Parser()
    parse_tree = p.parse(message)

    translation = list()
    find_best_translation(parse_tree, translation)
    print(message)
    print(translation)
    answer = translation.join(" ")

    # return the formulated answer
    return answer



# when you run the code through terminal, this will allow Flask to work
if __name__ == '__main__':
    app.run()