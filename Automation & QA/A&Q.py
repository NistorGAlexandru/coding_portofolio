from selenium import webdriver
from selenium.webdriver.common.by import By
import time

url = "https://www.link-academy.com/"

driver = webdriver.Chrome()

driver.get(url)

ID_ACCEPT_BUTTON = "politikaOK"
accept_button = driver.find_element(By.ID, ID_ACCEPT_BUTTON)
accept_button.click()

xpath_link = "/html/body/div[1]/nav/div[3]/ul/li[2]/a"
link = driver.find_element(By.XPATH, xpath_link)
link.click()
time.sleep(3)


ID_ACCEPT_BUTTON2 = "zatvori"
accept_button = driver.find_element(By.ID, ID_ACCEPT_BUTTON2)
accept_button.click()
time.sleep(2)

xpath_link2 = "/html/body/div[2]/aside/nav/div/div[2]/a[1]"
link2 = driver.find_element(By.XPATH, xpath_link2)
link2.click()
time.sleep(1)

xpath_link3 = "/html/body/div[2]/div[1]/div[2]/table[2]/tbody/tr[5]/td[3]/a"

link3 = driver.find_element(By.XPATH, xpath_link3)
link3.click()

input()

driver.quit()

