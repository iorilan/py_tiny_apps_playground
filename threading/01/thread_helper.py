import threading
import concurrent.futures
import queue
import traceback
import time
from threading import Timer

"""
    daemon task: [operation, (params..)]
"""
def wait_all(tasks):
    threads = []
    for t in tasks:
        x = threading.Thread(target=t[0], args=t[1], daemon=True)
        threads.append(x)
        x.start()

    for i,t in enumerate(threads):
        t.join()
        print(f'thread {i} finished')

    print(f'all done')

_target=30
def producer_consumer(num_producer,num_consumder,target=30):
    _target = target
    q=queue.Queue(maxsize=50)

    def prod(id):
        global _target
        try:
            while _target>0:
                i=time.time()
                q.put(i)
                print(f'[producer:{id}] produced {i}')
                time.sleep(1)
        except:
            traceback.print_exc()
            print(f'exception from id : prod{id}')
        print(f'producer {id} exit')

    def cons(id):
        global _target
        try:
            while _target > 0:
                if not q.empty():
                    i = q.get()
                    print(f'[consumder:{id}] consumed {i}. [target left : {_target}] left. [{q.qsize()}] in queue')
                    _target -= 1
                time.sleep(1)
        except:
            traceback.print_exc()
            print(f'exception from consumer id:{id}')
        print(f'consumer {id} exit')
    
    threads = []
    for i in range(num_producer):
        t = threading.Thread(target=prod, args=(i,), daemon=True)
        threads.append(t)
        t.start()
    for i in range(num_consumder):
        t = threading.Thread(target=cons, args=(i,), daemon=True)
        threads.append(t)
        t.start()
    
    for t in threads:
        t.join()
    
    print('exiting...')

    """
    Tried ThreadPoolExecutor , it is not daemon thread 
    https://stackoverflow.com/questions/49992329/the-workers-in-threadpoolexecutor-is-not-really-daemon
    with concurrent.futures.ThreadPoolExecutor(max_workers=10) as exe:
        for i in range(num_producer):
            exe.submit(prod,event, i)
            print(f'producer[{i}] started')
        for i in range(num_consumder):
            exe.submit(cons,event,i)
            print(f'consumer[{i}] started')
    """

_state=0
_lock = threading.Lock()
def racing(lock=True):
    def inc_nolock():
        global _state
        s=_state
        s+=1
        time.sleep(0.2)
        _state = s
        print(f'[no lock] state : {_state}')

    def inc_with_lock():
        global _state,_lock
        
        with _lock:
            s=_state
            s+=1
            time.sleep(0.2)
            _state = s
        print(f'[with lock] state: {_state}')

    if lock:

        t1= threading.Thread(target=inc_with_lock,args=())
        t2= threading.Thread(target=inc_with_lock,args=())
        t1.start()
        t2.start()
        t1.join()
        t2.join()
    else:
        t1= threading.Thread(target=inc_nolock,args=())
        t2= threading.Thread(target=inc_nolock,args=())
        t1.start()
        t2.start()
        t1.join()
        t2.join()
    print(f'racing demo finished. with lock :{lock}')
    

"""
    run function every n seconds
"""
class timer_func(Timer):
    def run(self):
        while not self.finished.wait(self.interval):
            self.function(*self.args, **self.kwargs)


