from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException

option = webdriver.ChromeOptions()
option.add_argument(" — incognito")

browser = webdriver.Chrome(executable_path="./chromedriver", chrome_options=option)
url="https://www.daraz.com.np/smartphones/"

def get_pages():
    browser.get("https://www.daraz.com.np/smartphones/")
    upperlimit=browser.find_element_by_xpath("//div/div[3]/div[1]/div/div[1]/div[1]/div/div[1]/div/div/span[1]")
    number = upperlimit.text
    number=int(number.split()[0])
    return (int(number/10))

pages=get_pages()

name_price_url= {}

def updatedict(dict):
    name_price_url.update(dict)


for i in range(1,3):
    browser.get("https://www.daraz.com.np/smartphones/?page={}".format(i))
    phone_name = browser.find_elements_by_xpath("//a[@ age='0']")
    phone_img = browser.find_elements_by_xpath('//div[@class="c2p6A5"]')
    phone_price = browser.find_elements_by_xpath("//span[@ class='c29VZV']")
    phone_link=[]
    name_price_url_tmp={}
    for item in phone_img:
        img=item.find_element_by_tag_name('a')
        link=img.get_attribute('href')
        phone_link.append(link)

    titles = [x.text for x in phone_name]
    price_list = [x.text for x in phone_price]

    titles_filtered= list(filter(None,titles))
    name_price_url_tmp=dict(zip(titles_filtered,zip(price_list,phone_link)))
    name_price_url.update(name_price_url_tmp)
    updatedict(name_price_url_tmp)

    print(len(name_price_url_tmp), len(name_price_url))
