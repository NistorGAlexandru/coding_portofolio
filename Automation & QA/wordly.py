from selenium import webdriver
from selenium.webdriver.common.by import By
import time

browser = webdriver.Chrome()
browser.get("https://wordly.org/")

characters = ["qwertyuiop", "asdfghjkl", " zxcvbnm "]

def get_row_button_index(ch):
    for row_index, line in enumerate(characters):
        if ch in line:
            return row_index, line.index(ch)    


words = ["audio", "stern", "glyph", 'words', 'place'] 

for word in words:
    for ch in word:
        y_row, y_poz =  get_row_button_index(ch)

        rows =  browser.find_elements(By.CLASS_NAME, "Game-keyboard-row")
        buttons =  rows[y_row].find_elements(By.CLASS_NAME, "Game-keyboard-button")
        buttons[y_poz].click()

        enter = rows[-1].find_elements(By.CLASS_NAME, "Game-keyboard-button")[-1]
        enter.click()

input()