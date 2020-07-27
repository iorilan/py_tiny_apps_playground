"""
    http://the-internet.herokuapp.com/login
"""
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
def go():
    # to keep browser open by passing in below option
    ops = Options()
    ops.add_experimental_option('detach',True)
    browser = webdriver.Chrome(ChromeDriverManager().install(),chrome_options=ops)

    browser.get("http://the-internet.herokuapp.com/login")
    
    username = browser.find_element_by_id("username")
    username.send_keys("tomsmith")
    password = browser.find_element_by_id("password")
    password.send_keys("SuperSecretPassword!")
    btn = browser.find_elements_by_css_selector(".radius")
    btn[0].click()


if __name__ == "__main__":
    go()