from selenium import webdriver
from selenium.webdriver.common.by import By
import time
from datetime import datetime

datetime.now().year

url = 'https://www.bereciucas.ro/'
driver = webdriver.Chrome()
driver.get(url)
time.sleep(5)

cookies_button = 'CybotCookiebotDialogBodyLevelButtonLevelOptinAllowAll'
accept_button = driver.find_element(By.ID, cookies_button)
accept_button.click()
time.sleep(5)

digit_inputs = driver.find_elements(By.CLASS_NAME, 'year-char')
year = datetime.now().year - 18
year = str(year)

for index, ch in enumerate(year):
    digit_inputs[index].send_keys(ch)

month = datetime.now().month
month = str(month).zfill(2)
driver.find_element(By.CLASS_NAME, 'month').send_keys(month)

day = datetime.now().day
day = str(day).zfill(2)

driver.find_element(By.CLASS_NAME, 'day').send_keys(day)

input()
driver.quit()