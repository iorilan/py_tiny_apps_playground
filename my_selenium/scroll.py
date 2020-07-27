"""
    http://the-internet.herokuapp.com/infinite_scroll
"""

from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
import time

def go():
    y=100
    # to keep browser open by passing in below option
    ops = Options()
    ops.add_experimental_option('detach',True)
    browser = webdriver.Chrome(ChromeDriverManager().install(),chrome_options=ops)

    browser.get("http://the-internet.herokuapp.com/infinite_scroll")
    
    
    while(True):
        time.sleep(0.3)
        browser.execute_script(f'window.scrollTo(0, {y})') 
        y+=10


if __name__ == "__main__":
    go()