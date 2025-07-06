from selenium import webdriver
from selenium.webdriver.common.by import By

url = 'https://techy-api.vercel.app/api/text'

driver = webdriver.Chrome()

driver.get(url)


body = driver.find_element(By.TAG_NAME, 'body')
print(body.text)