import time
#import systemd.daemon
import logging, logging.handlers as handlers

logger = logging.getLogger("log_app")
logger.setLevel(logging.DEBUG)

formatter = logging.Formatter('%(asctime)s - %(message)s')
handler = handlers.RotatingFileHandler("/the/path/to/test_log/file.log", maxBytes=1000, backupCount=1)
handler.setLevel(logging.DEBUG)
handler.setFormatter(formatter)

logger.addHandler(handler)

def echo(msg):
    logger.debug(msg)
    print(msg)    
if __name__ == '__main__':
    echo("init")
    time.sleep(1)

    # if Type=notify use below line
    #systemd.daemon.notify("READY=1")
    echo("started")
