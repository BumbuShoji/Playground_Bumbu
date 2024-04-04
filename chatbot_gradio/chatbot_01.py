#make chat bot using gradio and gpt
# -*- coding: utf-8 -*-
import gradio as gr
import openai
import os

openai.api_key = os.getenv("OPENAI_API_KEY")

#store talk memory
message_history = []

#def chatbot
def chatbot(message):
    #add user message to history
    message_history.append({"role": "user", "content": message})
    #get response from openai
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=message_history
    )
    #add chatbot response to history
    message_history.append({"role": "system", "content": response.choices[0].message})
    #return chatbot response
    return response.choices[0].message

#gradio interface
with gr.Interface(fn=chatbot, inputs="text", outputs="text") as iface:
    iface.launch()
