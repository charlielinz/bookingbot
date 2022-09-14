from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time
import json

with open("inline.json") as jsonfile:
    inline_url = json.load(jsonfile)

orders = [
    {
        "restaurant": "旨樂",
        "persons": {
            "adults": "3",
            "kids": "1"
        },
        "date": "09-20",
        "time": "18:00"
    }
]
driver = webdriver.Chrome("/Users/charlielin/repos/bookingbot/chromedriver")
index = 0
for order in orders:
    restaurant = order["restaurant"]
    adults = order["persons"]["adults"]
    kids = order["persons"]["kids"]
    persons = adults + kids
    date = order["date"]
    time_ = order["time"]

    driver.execute_script(
        f"window.open('{inline_url[restaurant]}', 'tab{index}')")
    driver.switch_to.window(f"tab{index}")
    time.sleep(3)
    driver.find_element(
        By.XPATH, f"//select[@id='adult-picker']/option[@value='{adults}']").click()
    driver.find_element(
        By.XPATH, f"//select[@id='kid-picker']/option[@value='{kids}']").click()
    time.sleep(2)
    driver.find_element(By.XPATH, "//div[@id='date-picker']").click()
    
    index += 1
