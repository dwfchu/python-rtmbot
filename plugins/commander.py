import time
import globalstatic
from sftp_sync import SFTPLocal

outputs = []
crontabs = []

tasks = {}

def process_message(data):
    global tasks
    channel = data["channel"]
    text = data["text"]

    def string_list(word_list,a_string):

        for k in word_list:
            if k in a_string:
                return True
        else: False


    if channel == globalstatic.main_channel:
        if globalstatic.main_channel in text or channel == globalstatic.main_channel:

            #tell time
            key_words = globalstatic.command_key
            if string_list(key_words,text):

                key_words = ["time"]
                if string_list(key_words, text):
                    outputs.append([channel,"The current time is " + time.asctime( time.localtime(time.time()))])

                key_words = ["print"]
                if string_list(key_words, text):
                    outputs.append([channel,"I am printing"])

                key_words = ["deploy"]
                if string_list(key_words, text):
                    outputs.append([channel,"I am performing synchronisation tasks....please wait"])

                    status, list = SFTPLocal.do_sync()

                    if status:
                        if len(list) > 0:
                            outputs.append([channel,"synchronisation complete, the following directories were successfully copied: \n" + '\n'.join(list)])
                        else:
                            outputs.append([channel,"synchronisation complete,no new directories were found"])
                    else:
                        outputs.append([channel,"synchronisation failed, please consult logs for more information"])



