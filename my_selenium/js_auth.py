"""
    http://the-internet.herokuapp.com/basic_auth
    easier way : pass the credential through url
"""

from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
import time
def go():
    # to keep browser open by passing in below option
    ops = Options()
    ops.add_experimental_option('detach',True)
    browser = webdriver.Chrome(ChromeDriverManager().install(),chrome_options=ops)

    browser.get("http://admin:admin@the-internet.herokuapp.com/basic_auth")
    


if __name__ == "__main__":
    go()