"""
    textbox/textarea
    checkbox
    radiobutton
    dropdown

    datetime

    listbox

    upload file 
    download file

    https://www.seleniumeasy.com/test/basic-first-form-demo.html
"""
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
import os
def text():
    ops = Options()
    ops.add_experimental_option('detach',True)
    browser = webdriver.Chrome(ChromeDriverManager().install(),chrome_options=ops)

    browser.get("https://www.seleniumeasy.com/test/basic-first-form-demo.html")
    
    txt = browser.find_element_by_id("user-message")
    txt.send_keys("aaabbb")
    btn = browser.find_elements_by_css_selector("#get-input button")[0]
    btn.click()
    label = browser.find_element_by_id("display")
    print(label.text)

def checkbox():
    ops = Options()
    ops.add_experimental_option('detach',True)
    browser = webdriver.Chrome(ChromeDriverManager().install(),chrome_options=ops)

    browser.get("https://www.seleniumeasy.com/test/basic-checkbox-demo.html")
    
    chk = browser.find_element_by_id("isAgeSelected")
    chk.click()
    chkArr = browser.find_elements_by_css_selector(".cb1-element")
    chkArr[0].click()
    chkArr[1].click()
    
def radiobutton():
    ops = Options()
    ops.add_experimental_option('detach',True)
    browser = webdriver.Chrome(ChromeDriverManager().install(),chrome_options=ops)

    browser.get("https://www.seleniumeasy.com/test/basic-radiobutton-demo.html")
    
    radioArr1 = browser.find_elements_by_css_selector("input[name=optradio]")
    radioArr1[0].click()
    btn1 = browser.find_element_by_id("buttoncheck")
    btn1.click()
    label1 = browser.find_elements_by_css_selector(".radiobutton")[0]
    print(label1.text)

    radioArr2 = browser.find_elements_by_css_selector("input[name=gender]")
    radioArr2[1].click()
    
    radioArr3 = browser.find_elements_by_css_selector("input[name=ageGroup]")
    radioArr3[2].click()
    
    btn2 = browser.find_elements_by_css_selector(".btn-default")[1]
    btn2.click()    
    label2 = browser.find_elements_by_css_selector(".groupradiobutton")[0]
    print(label2.text)

def fillform():
    ops = Options()
    ops.add_experimental_option('detach',True)
    browser = webdriver.Chrome(ChromeDriverManager().install(),chrome_options=ops)

    browser.get("https://www.seleniumeasy.com/test/input-form-demo.html")
    
    def fill(css, val):
        obj = browser.find_elements_by_css_selector(css)[0]
        obj.send_keys(val)
    fill("input[name=first_name]", "aaa")
    fill("input[name=last_name]", "aaa")
    fill("input[name=email]", "aaa")
    fill("input[name=phone]", "aaa")
    fill("input[name=address]", "aaa")
    fill("input[name=city]", "city")
    fill("input[name=zip]", "bbb")
    fill("input[name=website]", "website")
    fill("textarea[name=comment]", "comment")

    browser.find_element_by_xpath("//select[@name='state']/option[text()='Alaska']").click()
    browser.find_elements_by_css_selector("input[name=hosting]")[1].click()
    
    browser.find_elements_by_css_selector("button[type=submit]")[0].click()
def date_select():
    ops = Options()
    ops.add_experimental_option('detach',True)
    browser = webdriver.Chrome(ChromeDriverManager().install(),chrome_options=ops)

    browser.get("https://www.seleniumeasy.com/test/bootstrap-date-picker-demo.html")
    
    dt1 = browser.find_elements_by_css_selector(".input-group input")[0]
    dt1.click()
    browser.find_elements_by_css_selector(".day")[0].click()

    
    dt2 = browser.find_elements_by_css_selector("#datepicker input")[0]
    dt2.click()
    print(f'before:{dt2.get_attribute("value")}')
    browser.find_elements_by_css_selector(".day")[-1].click() # from
    print(f'after:{dt2.get_attribute("value")}')


    
    dt3 = browser.find_elements_by_css_selector("#datepicker input")[1]
    dt3.click()
    print(f'before: {dt3.get_attribute("value")}')
    browser.find_elements_by_css_selector(".new")[2].click() # to
    print(f'after : {dt3.get_attribute("value")}')

def listbox():
    ops = Options()
    ops.add_experimental_option('detach',True)
    browser = webdriver.Chrome(ChromeDriverManager().install(),chrome_options=ops)

    browser.get("https://www.seleniumeasy.com/test/jquery-dual-list-box-demo.html")
    
    browser.find_element_by_xpath("//select[@class='form-control pickListSelect pickData']/option[text()='Isis']").click()
    browser.find_element_by_xpath("//select[@class='form-control pickListSelect pickData']/option[text()='Julia']").click()
    browser.find_elements_by_css_selector(".pAdd")[0].click()
    res = browser.find_elements_by_css_selector(".pickListResult")[0]
    print(res.text)


def file_upload():
    ops = Options()
    ops.add_experimental_option('detach',True)
    browser = webdriver.Chrome(ChromeDriverManager().install(),chrome_options=ops)

    browser.get("http://the-internet.herokuapp.com/upload")
    browser.find_element_by_id("file-upload").send_keys(os.getcwd()+"/readme.txt")
    browser.find_element_by_id("file-submit").click()

if __name__ == "__main__":
    #text()
    #checkbox()
    #radiobutton()
    #fillform()
    #date_select()
    #listbox()
    file_upload()