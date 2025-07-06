from selenium.webdriver import Chrome
from selenium.webdriver.common.by import By
import time
url = "http://127.0.0.1:8000/"



browser = Chrome()
browser.get(url)

input_cnp = browser.find_element(By.ID, "id_cnp")
input_cnp.send_keys("299021946900")


time.sleep(3)

input_send = browser.find_element(By.ID, "id_send")
input_send.click()

time.sleep(3)

h2_element =  browser.find_element(By.TAG_NAME, "h2")



assert "Are access" in h2_element.text 

browser.quit()
