import pysftp
from log import log

class estConnection():

    def __init__(self,hostname="",username="",password="",port=22):
        self.host = hostname
        self.username = username
        self.password = password
        self.port = port

    def openConn(self):

        try:
            conn = pysftp.Connection(host=self.host, username=self.username, password=self.password,port=self.port)
            log.info('Connection: ' + self.host + ':' + str(self.port) + ' established successfully')
            return conn
        except:
            log.info('Error on connection: ' + self.host + ':' + str(self.port))


    def closeConn(self):

        self.close()

def closeConnections(conn):
    #close connections

    try:
        conn.close()
        log.info('Connection closed')
    except:
        log.info('Connection close failed')
