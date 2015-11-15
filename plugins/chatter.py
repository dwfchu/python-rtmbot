import time
import globalstatic

from chatterbot import ChatBot

chatbot = ChatBot("bigdata_bot")
# Train based on the english corpus
chatbot.train("chatterbot.corpus.english")
# Train based on english greetings corpus
chatbot.train("chatterbot.corpus.english.greetings")
# Train based on the english conversations corpus
chatbot.train("chatterbot.corpus.english.conversations")

outputs = []
crontabs = []

tasks = {}

def process_message(data):
    global tasks
    channel = data["channel"]
    text = data["text"]
    channel_tag = ('<@' + globalstatic.main_channel +'>')

    def string_list(word_list,a_string):
        return set(word_list).intersection(a_string.split())

    #only accept on bigdata_playpen
    if channel == globalstatic.main_channel:
        if channel_tag in text or channel == globalstatic.main_channel:
            if globalstatic.command_key not in text:
                outputs.append([channel,chatbot.get_response(text.replace(channel_tag,""))])
