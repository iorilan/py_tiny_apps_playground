"""
    http://the-internet.herokuapp.com/drag_and_drop
    https://www.seleniumeasy.com/test/drag-and-drop-demo.html

    the drag drop only works with js helper 
"""
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
import time

from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait as wait
from selenium.webdriver.common.action_chains import ActionChains as ac

def drag_drop(driver,source,target):
    with open("drag_drop_helper.js") as f:
        js = f.read()
        driver.execute_script(js + "$('"+source+"').simulateDragDrop({ dropTarget: '"+target+"'});")

def go():
    # to keep browser open by passing in below option
    ops = Options()
    ops.add_experimental_option('detach',True)
    browser = webdriver.Chrome(ChromeDriverManager().install(),chrome_options=ops)

    browser.get("http://the-internet.herokuapp.com/drag_and_drop")
    wait(browser, 10).until(EC.presence_of_element_located((By.ID, "column-a")))
    
    # source = browser.find_elements_by_css_selector('#column-a')[0]
    # target = browser.find_elements_by_css_selector('#column-b')[0]
    #NOT WORKING :
    #ac(browser).drag_and_drop(source,target).perform()
    #ac(browser).click_and_hold(source).move_to_element(target).release(source).perform()
    #NOT WORKING

    drag_drop(browser,"column-a", "column-b")
    
def demo2():
    ops = Options()
    ops.add_experimental_option('detach',True)
    browser = webdriver.Chrome(ChromeDriverManager().install(),chrome_options=ops)

    browser.get("https://www.seleniumeasy.com/test/drag-and-drop-demo.html")
    wait(browser, 10).until(EC.presence_of_element_located((By.ID, "todrag")))

    
    drag_drop(browser, "#todrag span", "#mydropzone")



if __name__ == "__main__":
    #go()
    demo2()