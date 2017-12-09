import logging
import os
import sys
from Crypto.Cipher import DES




DBPATH   ='mongodb://localhost:27017/'

ONLINEUSERS={}
CONECTIONS= []
TCP=3131
UDP=5151
ROOTPATH = ''
COLLECTIONS="authentication"
DBNAME="P2PApp"
TIMEOUT=60
DES_=DES.new('qwe123ac', DES.MODE_CFB, b'\x17E;5[v\xdc\x8a')






for i in os.path.dirname(os.path.abspath(__file__)).split('/')[1:]:
        ROOTPATH = ROOTPATH+'/'+i
if ROOTPATH not in sys.path:
        sys.path.append(ROOTPATH)

def getlog():
    logFormatter = logging.Formatter(
        "%(asctime)s [%(filename)s  %(funcName)s  %(threadName)s ] [%(levelname)-5.5s]  %(message)s")
    rootLogger = logging.getLogger()

    if (len(rootLogger.handlers) > 0):
        return rootLogger
    rootLogger.setLevel(logging.INFO)
    fileHandler = logging.FileHandler(ROOTPATH+'/logfile.log')
    fileHandler.setFormatter(logFormatter)
    rootLogger.addHandler(fileHandler)
    consoleHandler = logging.StreamHandler()
    consoleHandler.setFormatter(logFormatter)
    rootLogger.addHandler(consoleHandler)
    return rootLogger