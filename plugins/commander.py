import time

outputs = []
crontabs = []

tasks = {}

def process_message(data):
    global tasks
    channel = data["channel"]
    text = data["text"]

    def string_list(word_list,a_string):
        return set(word_list).intersection(a_string.split())

    #only accept on bigdata_playpen
    if channel == 'C0EA4CNRG':
        if "<@U0E7M8BV1>" in data["text"]:
            #say hi
            key_words = ["hello","hey","yo"]
            if string_list(key_words, text):
                outputs.append([channel,"Hey you!" ])

            #tell time
            key_words = ["time"]
            if string_list(key_words, text):
                outputs.append([channel,"The current time is " + time.asctime( time.localtime(time.time()))])


