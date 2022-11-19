import time
import os

INFO='INFO'
WARN='WARN'
ERROR='ERROR'

def log(msg,mode='INFO'):
    msg,mode=str(msg),str(mode)

    logfile=open('debug.log','a')
    logfile.write('{0} [{1}]-{2}\t{3}\n'.format(time.ctime(),mode[0].upper(),mode,msg))

def clear_log():
    os.remove('debug.log')

if __name__ == '__main__':
    clear_log()