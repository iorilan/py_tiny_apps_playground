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

    browser.get("http://the-internet.herokuapp.com/windows")
    #open tab
    txt = browser.find_elements_by_link_text("Click Here")[0]
    txt.click()

    browser.switch_to.window(browser.window_handles[-1])
    newtab = browser.find_elements_by_css_selector(".example")[0]
    print(newtab.text) # New Window

if __name__ == "__main__":
    go()