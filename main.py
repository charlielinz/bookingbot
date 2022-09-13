from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time, json

with open("inline.json") as jsonfile:
    inline_url = json.load(jsonfile)
    
order = ["fermi", "fermi", "旨樂"]
driver = webdriver.Chrome("/Users/charlielin/repos/bookingbot/chromedriver")
index = 0
for restaurant in order:
    driver.execute_script(f"window.open('{inline_url[restaurant]}', 'tab{index}')")
    driver.switch_to.window(f"tab{index}")
    index += 1

# search_input = driver.find_element(By.NAME, 'q')
# search_input.send_keys("inline")
# search_input.send_keys(Keys.ENTER)
