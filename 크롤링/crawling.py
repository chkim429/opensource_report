from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

browser = webdriver.Chrome('C:/chromedriver.exe')
browser.get('https://www.naver.com')


browser.find_element_by_xpath('//*[@id="NM_FAVORITE"]/div[1]/ul[1]/li[5]/a').click()


search = browser.find_element_by_xpath('//*[@id="_verticalGnbModule"]/div/div[2]/div/div[2]/div/div[2]/form/fieldset/div/input')
search.click()
time
search.send_keys('애플워치7')
search.send_keys(Keys.ENTER)

last_height = browser.execute_script("return document.body.scrollHeight")

while True:
    browser.execute_script("window.scrollTo(0, document.body.scrollHeight);")
    time.sleep(1)

    new_height = browser.execute_script("return document.body.scrollHeight")
    if new_height == last_height:
        break
    last_height = new_height
    
    
mearchs = browser.find_elements_by_css_selector(".basicList_info_area__17Xyo")

for mearch in mearchs:
    name = mearch.find_element_by_css_selector(".basicList_title__3P9Q7").text
    price = mearch.find_element_by_css_selector(".price_num__2WUXn").text
    link = mearch.find_element_by_css_selector(".basicList_title__3P9Q7 > a").get_attribute('href')
    
    print(name,price,link)
