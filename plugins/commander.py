import time
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

    # Get a response to an input statement
    #chatbot.get_response("Hello, how are you today?")

    def string_list(word_list,a_string):
        return set(word_list).intersection(a_string.split())

    #only accept on bigdata_playpen
    # if channel == 'C0EA4CNRG':
    if channel == 'D0EA1QUE7':
        # if "<@U0E7M8BV1>" in data["text"]:
        if "<@D0EA1QUE7>" in data["text"] or channel == "D0EA1QUE7":

            # outputs.append([channel,chatbot.get_response(text.replace("<@U0E7M8BV1>",""))])
            if "--" not in text:
                outputs.append([channel,chatbot.get_response(text.replace("<@D0EA1QUE7>",""))])
