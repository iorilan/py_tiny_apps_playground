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

    browser.get("http://the-internet.herokuapp.com/login")
    #open tab
    browser.execute_script('window.open("http://stackoverflow.com")')

    #open another tab
    browser.execute_script('window.open("http://google.com")')
    
    time.sleep(3)
    browser.quit()
    
    
    


if __name__ == "__main__":
    go()