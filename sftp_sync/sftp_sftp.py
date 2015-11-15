import pysftp
from log import log
import os
import shutil
import datetime
import sftp_connector

local_dir = 'local'

def closeConnections(conn):
    #close connections

    try:
        conn.close()
        log.info('Connection closed')
    except:
        log.info('Connection close failed')

def syncProcess():

    src_file_names = []
    tar_file_names = []

    #open source connection
    src_conn_set = sftp_connector.estConnection("localhost","sftp_usr","Password1")
    src_conn = src_conn_set.openConn()

    # #open target connection
    # tar_conn_set = estConnection("localhost","sftp_usr2","Password1",33)
    # tar_conn = tar_conn_set.openConn()

    # Get the directory and file listing
    data_src = src_conn.listdir()
    data_tar = tar_conn.listdir()

    # Add source files to sync list
    for i in data_src:
        if src_conn.isdir(i):
            src_file_names.append(i)

    # Add target to sync list
    for i in data_tar:
        if tar_conn.isdir(i):
            tar_file_names.append(i)

    #compare
    copyList = list(set(src_file_names) - set(tar_file_names))
    copyListLen = len(copyList)

    if  copyListLen > 0:
        log.info(str(copyListLen) + ' directories to be copied...')
        for copy_dir_name in copyList:

            if src_conn.isdir(copy_dir_name):

                #remove local dir
                checkLocal_content(copy_dir_name)

                src_conn.get_r(copy_dir_name, 'local')
                log.info(copy_dir_name + ' downloaded')
    else:
        log.info('All folders in sync...nothing to do')

    #close connections
    log.info('Source connection status: ' + src_conn_set.host + ':' + str(src_conn_set.port))
    closeConnections(src_conn)
    log.info('Target connection status: ' + tar_conn_set.host + ':' + str(tar_conn_set.port))
    closeConnections(tar_conn)


def checkLocal_main():

    global local_dir

    if not os.path.exists(local_dir):
        os.makedirs(local_dir)

def checkLocal_content(content_name):

    if os.path.exists(local_dir + "/" + content_name):
        log.info('Local folder does not exist, creating...')
        shutil.rmtree(local_dir + '/' + content_name)
        log.info('Local folder created...')

def logShutdown(status):

    if status == 1:
        log.info('Application exited successfuly @ ' + str(datetime.datetime.now()))
    else:
        log.info('Application exited with failure @ ' + str(datetime.datetime.now()))

    log.info('\n')

def do_sync():
    try:
        #check and create local staging directory
        checkLocal_main()
        #initiate check and copy process
        syncProcess()
        logShutdown(1)
    except:
        logShutdown(0)







