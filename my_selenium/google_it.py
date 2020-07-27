"""
    google something and click enter
"""

from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.keys import Keys

def go(searching):
    # to keep browser open by passing in below option
    # ops = Options()
    # ops.add_experimental_option('detach',True)
    # browser = webdriver.Chrome(ChromeDriverManager().install(),chrome_options=ops)

    browser = webdriver.Chrome(ChromeDriverManager().install())
    browser.get("https://www.google.com")

    txt_search = browser.find_element_by_name("q")
    txt_search.send_keys(searching)

    txt_search.send_keys(Keys.ENTER)


if __name__ == "__main__":
    print('search what?')
    go(input())
    
    print('click anything to exit')