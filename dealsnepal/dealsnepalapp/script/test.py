from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
import json
from pyvirtualdisplay import Display
from selenium.webdriver.common.keys import Keys
import time

def scrollDown(browser):
    body = browser.find_element_by_tag_name("body")
    body.send_keys(Keys.PAGE_DOWN)
    return browser


url="https://www.daraz.com.np/smartphones/"

option = webdriver.ChromeOptions()
option.add_argument(" — incognito")

browser = webdriver.Chrome(executable_path="./chromedriver", chrome_options=option)
browser.get("https://www.daraz.com.np/smartphones/")
phone_img = browser.find_elements_by_tag_name('img')
scrollDown(browser)
for x in phone_img:
    print(x.get_attribute('src'))

browser.get("https://www.daraz.com.np/smartphones/")
phone_img1 = browser.find_elements_by_tag_name('img')
for x in phone_img1:
    print(x.get_attribute('src'))







#
# def get_pages():
#     browser.get("https://www.daraz.com.np/smartphones/")
#     upperlimit=browser.find_element_by_xpath("//div/div[3]/div[1]/div/div[1]/div[1]/div/div[1]/div/div/span[1]")
#     number = upperlimit.text
#     number=int(number.split()[0])
#     return (int(number/10))

#pages=get_pages()
#
# name_price_url= {}
#
# def updatedict(dict):
#     name_price_url.update(dict)
#
#
# # lenOfPage = browser.execute_script("window.scrollTo(0, document.body.scrollHeight);var lenOfPage=document.body.scrollHeight;return lenOfPage;")
# # match=False
# # while(match==False):
# #     lastCount = lenOfPage
# #     time.sleep(.5)
# #     lenOfPage = browser.execute_script("window.scrollTo(0, document.body.scrollHeight);var lenOfPage=document.body.scrollHeight;return lenOfPage;")
# #     if lastCount==lenOfPage:
# #         match=True
#
# #
# # phone_name = browser.find_elements_by_xpath("//a[@ age='0']")
# #
# # phone_img = browser.find_elements_by_tag_name('img')
# #
#
# elem = browser.find_element_by_tag_name("body")
# no_of_pagedowns = 10
#
# while no_of_pagedowns:
#
#     elem.send_keys(Keys.PAGE_DOWN)
#     time.sleep(0.2)
#     no_of_pagedowns -= 1
#     print(elem)
#     print(len(elem))
#         #print(len(name_price_url_tmp), len(name_price_url))
#
#
# #
# # with open('smartphones.json','w') as jsonfile:
# #     json.dump(name_price_url,jsonfile, indent=4)
