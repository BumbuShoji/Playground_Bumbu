# -*- coding: utf-8 -*-
# This program is aim to create chatbot in telegram

import os
import json
import boto3
import openai
import telebot
from dotenv import load_dotenv

load_dotenv()
bot = telebot.TeleBot(os.getenv("TELEGRAM_TOKEN"))
openai.api_key = os.getenv("OPENAI_API_KEY")

class Chatbot:
    def __init__(self):
        self.chatbot = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=[
                {
                    "role": "system",
                    "content": "You are a helpful assistant."
                }
            ]
        )

    def send_message(self, message):
        response = openai.ChatCompletion.create(
            model="gpt-3.0",
            messages=[
                {
                    "role": "system",
                    "content": "You are a helpful assistant."
                },
                {
                    "role": "user",
                    "content": message
                }
            ]
        )
        return response.choices[0].message

    def run(self):
        @bot.message_handler(func=lambda message: True)
        def send_message(message):
            response = self.send_message(message.text)
            bot.reply_to(message, response)

if __name__ == "__main__":
    chatbot = Chatbot()
    chatbot.run()