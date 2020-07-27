"""
    click on javascript alert
    http://the-internet.herokuapp.com/javascript_alerts
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

    browser.get("http://the-internet.herokuapp.com/javascript_alerts")
    result = browser.find_elements_by_id("result")[0]

    btn = browser.find_elements_by_tag_name("button")
    btn[0].click() #  click alert
    time.sleep(1)
    browser.switch_to_alert().accept()
    print(result.get_attribute("outerHTML"))
    print(result.text)

    btn[1].click() # confirm
    time.sleep(1)
    browser.switch_to_alert().dismiss()
    print(result.text)

    btn[2].click()
    time.sleep(1)
    cfm_alert = browser.switch_to.alert
    cfm_alert.send_keys("abcd")
    cfm_alert.accept()
    print(result.text)


if __name__ == "__main__":
    go()