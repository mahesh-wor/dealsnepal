
from selenium import webdriver



def get_img_url(url):
    option = webdriver.ChromeOptions()
    option.add_argument("--headless")
    option.add_argument("--incognito")

    browser = webdriver.Chrome(executable_path="./chromedriver", chrome_options=option)

    browser.get(url)
    phone_img = browser.find_elements_by_xpath("//img[@ class='pdp-mod-common-image gallery-preview-panel__image']")
    for  x in phone_img:
        a=x.get_attribute("src").strip("_.webp")
        browser.quit()
    return a
