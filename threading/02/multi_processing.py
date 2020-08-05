
"""
    speed up using multi core
"""
import requests
import multiprocessing
import time

session = None


def set_global_session():
    global session
    if not session:
        session = requests.Session() 

def open_url(url):
    with session.get(url) as response:
        name = multiprocessing.current_process().name
        print(f"{name}:Read {len(response.content)} from {url}")

def open_all():
    urls = ["https://github.com/iorilan"]*50

    start = time.time()
    with multiprocessing.Pool(initializer=set_global_session) as pool:
        pool.map(open_url, urls)
    
    end = time.time()
    print(f'open {len(urls)} url .time used {round(end-start,2)} second')

if __name__ == "__main__":
    open_all()
    

    

    