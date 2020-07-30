import thread_helper as helper
import time 
import threading
import datetime

def run_many_wait_all():
    def t1(index):
        for i in range(10):
            print(f'[faster] thread {index} : i')
            time.sleep(0.5)
    def t2(index):
        for i in range(10):
            print(f'[slow] thread {index} : i')
            time.sleep(1)
    tasks = []
    tasks.append([t1, (1,)])
    tasks.append([t2, (2,)])
    helper.wait_all(tasks)


def timer_func():
    def print_time():
        print(datetime.datetime.now())
    timer = helper.timer_func(1, print_time)
    timer.start()
    time.sleep(10)
    timer.cancel()
    print(f'done')
    
if __name__ == "__main__":
    #run_many_wait_all()
    #helper.producer_consumer(4,2)
    #helper.racing(False)
    #timer_func()