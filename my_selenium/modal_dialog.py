"""
    click on bootstrap model diaglog
    https://www.seleniumeasy.com/test/bootstrap-modal-demo.html
"""

from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
import time

from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait as wait

def go():
    # to keep browser open by passing in below option
    ops = Options()
    ops.add_experimental_option('detach',True)
    browser = webdriver.Chrome(ChromeDriverManager().install(),chrome_options=ops)

    browser.get("https://www.seleniumeasy.com/test/bootstrap-modal-demo.html")
    time.sleep(2)
    btn_modal = browser.find_elements_by_link_text("Launch modal")
    #print(len(btn_modal))
    #popup 1st modal
    btn_modal[0].click()
    wait(browser, 3).until(EC.visibility_of_element_located((By.ID, "myModal0")))
    dialog1_btn=browser.find_elements_by_css_selector("#myModal0 .btn")
    
    #close
    dialog1_btn[0].click()
    
    #popup again
    time.sleep(1)
    btn_modal[0].click()
    
    #save and close
    time.sleep(1)
    dialog1_btn[1].click()
    



if __name__ == "__main__":
    go()