from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
import phone
import time
import json

option = webdriver.ChromeOptions()

browser = webdriver.Chrome(executable_path="./chromedriver", chrome_options=option)

browser.get("https://www.daraz.com.np/smartphones/")
script_name = browser.find_elements_by_xpath("//script[@ type='application/ld+json']").__getattribute__("innerhtml")
for x in script_name:

    print('hi/hello')