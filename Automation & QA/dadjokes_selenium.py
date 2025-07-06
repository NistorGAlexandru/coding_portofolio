from selenium import webdriver
from selenium.webdriver.common.by import By
import time

browser = webdriver.Chrome()
browser.get("https://icanhazdadjoke.com ")

time.sleep(1)
browser.find_element(By.CLASS_NAME, "fc-button-label").click()
time.sleep(1)

def read_joke():
      return browser.find_elements(By.CLASS_NAME, "subtitle")[1].text

def refresh_joke():
    browser.find_element(By.XPATH, "/html/body/section/div/div[1]/div[2]/a/span[2]").click()




with open("jokes.txt", "a") as fwriter:
    joke = read_joke()
    fwriter.write(joke + "\n")
    print(joke)
    for i in range(4):
        refresh_joke()
        time.sleep(4)
        joke = read_joke()
        print(joke)
        fwriter.write(joke + "\n")

input()
browser.quit()