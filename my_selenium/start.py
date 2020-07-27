"""
    pip install webdriver-manager
    try download latest driver and open chrome
"""

from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager

browser = webdriver.Chrome(ChromeDriverManager().install())
browser.get("https://www.google.com")
