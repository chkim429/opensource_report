from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

browser = webdriver.Chrome('C:/chromedriver.exe')
browser.get('https://www.naver.com')


browser.find_element_by_xpath('//*[@id="NM_FAVORITE"]/div[1]/ul[1]/li[5]/a').click()


search = browser.find_element_by_xpath('//*[@id="_verticalGnbModule"]/div/div[2]/div/div[2]/div/div[2]/form/fieldset/div/input')
search.click()
search.send_keys('애플워치7')
search.send_keys(Keys.ENTER)

last_height = browser.execute_script("return document.body.scrollHeight")

while True:
    # 끝까지 스크롤 내리기
    browser.execute_script("window.scrollTo(0, document.body.scrollHeight);")

    # 대기
    time.sleep(1)

    # 스크롤 내린 후 스크롤 높이 다시 가져옴
    new_height = browser.execute_script("return document.body.scrollHeight")
    if new_height == last_height:
        break
    last_height = new_height