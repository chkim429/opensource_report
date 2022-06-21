from selenium import webdriver
from selenium.webdriver.common.keys import Keys

browser = webdriver.Chrome('C:/chromedriver.exe')
browser.get('https://www.naver.com')


browser.find_element_by_xpath('//*[@id="NM_FAVORITE"]/div[1]/ul[1]/li[5]/a').click()


search = browser.find_element_by_xpath('//*[@id="_verticalGnbModule"]/div/div[2]/div/div[2]/div/div[2]/form/fieldset/div/input')
search.click()
search.send_keys('애플워치7')
search.send_keys(Keys.ENTER)