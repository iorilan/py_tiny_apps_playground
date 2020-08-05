
"""
    multi-thread with ThreadPoolExecutor
"""
import concurrent.futures
import requests
import threading
import time

thread_local = threading.local()

def get_session():
    if not hasattr(thread_local, "session"):
        thread_local.session = requests.Session()
    return thread_local.session

def open_url(url):
    session = get_session()
    with session.get(url) as response:
        print(f"Read {len(response.content)} from {url}")

if __name__ == "__main__":
    urls = [
        "https://github.com/iorilan"
    ]*50
    start = time.time()

    with concurrent.futures.ThreadPoolExecutor(max_workers=5) as exe:
        exe.map(open_url, urls)

    end = time.time()

    print(f'open {len(urls)} url .time used {round(end-start,2)} second')