import logging, time
import helper
import traceback

def time_log():
    log = helper.logger_minute()

    while True:
        log.info("test message ")
        print("log saved")
        time.sleep(20)

def default_log():
    log = helper.logger_default()
    while True:
        for i in range(20):
            log.debug("debuging log, a lot .")
            print('debuging logged')
            time.sleep(0.1)

        log.info("info log")
        print('info logged')
        
        try:
            1/0
        except:
            log.error(traceback.format_exc())
            print("error logged")
        
        time.sleep(10)

if __name__ == "__main__":
    default_log()
        
    
    