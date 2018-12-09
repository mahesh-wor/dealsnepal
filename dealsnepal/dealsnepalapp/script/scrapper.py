from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
import phone
import time
import json


option = webdriver.ChromeOptions()


option = Options()
option.add_argument("--headless")
option.add_argument("--incognito")

browser = webdriver.Chrome(executable_path="./chromedriver", chrome_options=option)
url="https://www.daraz.com.np/smartphones/"

def get_pages():
    browser.get("https://www.daraz.com.np/smartphones/")
    upperlimit=browser.find_element_by_xpath("//div/div[3]/div[1]/div/div[1]/div[1]/div/div[1]/div/div/span[1]")
    number = upperlimit.text
    number=int(number.split()[0])
    return (int(number/10))

pages=get_pages()

name_price_detail_url= {}

def updatedict(dict):
    name_price_detail_url.update(dict)


for i in range(1,4):
    browser.get("https://www.daraz.com.np/smartphones/?page={}".format(i))
    phone_name = browser.find_elements_by_xpath("//a[@ age='0']")
    phone_img = browser.find_elements_by_xpath('//div[@class="c2p6A5"]')
    phone_price = browser.find_elements_by_xpath("//span[@ class='c29VZV']")
    phone_img_url=[]
    phone_img_detail=[]
    name_price_url_tmp={}
    for item in phone_img:

        img=item.find_element_by_tag_name('a')
        link=img.get_attribute('href')

        url_tmp=phone.get_img_url(link)
        print(url_tmp)
        time.sleep(4)
        phone_img_url.append(url_tmp)

        phone_img_url.append(link)
        phone_img_detail.append(link)

        print(link)

    titles = [x.text.replace("/","") for  x in phone_name]
    price_list = [int(x.text.split()[1].replace(",","")) for x in phone_price]

    titles_filtered= list(filter(None,titles))
    name_price_url_tmp=dict(zip(titles_filtered,zip(price_list,phone_img_detail,phone_img_url)))
    #name_price_detail_url.update(name_price_url_tmp)

    updatedict(name_price_url_tmp)

print(name_price_detail_url)

with open('name_price_detail_url.json','w') as outfile:
    json.dump(name_price_detail_url,outfile)



