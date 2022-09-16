from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import pathlib
import time
import datetime

restaurant_to_url = {
    "fermizhenxinfen": "https://inline.app/booking/-M_4lh4XoLRZY0H4SZ7J:inline-live-2/-M_4lhEoT8tsZEPSjDJG?language=zh-tw",
    "zhiyue": "https://inline.app/booking/-Mcs0Z6qXFZ7YJ9vGZYp:inline-live-2/-Mcs0ZHAysFnkN98Djv3?language=zh-tw",
}

base_dir = pathlib.Path(__file__).resolve().parent
service = Service(base_dir / "chromedriver")


def book_fermizhenxinfen(order):
    restaurant = "fermizhenxinfen"
    adults = order["adults"]
    date = datetime.datetime.strptime(order["date"], "%Y/%m/%d").strftime("%Y-%m-%d")
    time_ = order["time"].replace(":", "-")
    name = order["name"]
    gender = order["gender"]
    phone = "0" + str(order["phone"])
    email = order["email"]
    purpose = order["purpose"]

    driver = webdriver.Chrome(service=service)
    driver.get(restaurant_to_url[restaurant])
    time.sleep(5)

    driver.find_element(By.XPATH, f"//select[@id='adult-picker']/option[@value='{adults}']").click()
    date_picker = driver.find_element(By.XPATH, "//div[@id='date-picker']")
    driver.execute_script("arguments[0].scrollIntoView(true);", date_picker)
    time.sleep(0.5)
    driver.execute_script("arguments[0].scrollIntoView(true);", date_picker)
    time.sleep(1)
    driver.find_element(By.XPATH, "//div[@id='date-picker']").click()
    time.sleep(0.5)
    driver.find_element(By.XPATH, f"//div[@data-date='{date}']").click()
    time.sleep(1.5)
    driver.find_element(By.CLASS_NAME, f"time-slot-{time_}").click()
    driver.find_element(By.XPATH, "//button[@data-cy='book-now-action-button']").click()
    time.sleep(5)

    driver.find_element(By.XPATH, "//input[@id='name']").send_keys(name)
    driver.find_element(By.XPATH, f"//input[@id='gender-{gender}']").click()
    driver.find_element(By.XPATH, "//input[@id='phone']").send_keys(phone)
    driver.find_element(By.XPATH, "//input[@id='email']").send_keys(email)
    driver.find_element(By.XPATH, f"//div[@value='{purpose}']").click()
    privacy_checkbox = driver.find_element(By.XPATH, "//input[@id='privacy-policy']")
    driver.execute_script("arguments[0].scrollIntoView(true);", privacy_checkbox)
    time.sleep(1)
    driver.find_element(By.XPATH, "//label[@for='privacy-policy']").click()
    driver.find_element(By.XPATH, "//button[@type='submit']").click()


def book_zhiyue(order):
    restaurant = "zhiyue"
    adults = order["adults"]
    kids = order["kids"]
    date = datetime.datetime.strptime(order["date"], "%Y/%m/%d").strftime("%Y-%m-%d")
    time_ = order["time"].replace(":", "-")
    name = order["name"]
    gender = order["gender"]
    phone = "0" + str(order["phone"])
    email = order["email"]
    purpose = order["purpose"]

    driver = webdriver.Chrome(service=service)
    driver.get(restaurant_to_url[restaurant])
    time.sleep(5)

    driver.find_element(By.XPATH, f"//select[@id='kid-picker']/option[@value='{kids}']").click()
    driver.find_element(By.XPATH, f"//select[@id='adult-picker']/option[@value='{adults}']").click()

    date_picker = driver.find_element(By.XPATH, "//div[@id='date-picker']")
    driver.execute_script("arguments[0].scrollIntoView(true);", date_picker)
    time.sleep(0.5)
    driver.execute_script("arguments[0].scrollIntoView(true);", date_picker)
    time.sleep(1)
    driver.find_element(By.XPATH, "//div[@id='date-picker']").click()
    time.sleep(0.5)
    driver.find_element(By.XPATH, f"//div[@data-date='{date}']").click()
    time.sleep(1.5)
    driver.find_element(By.CLASS_NAME, f"time-slot-{time_}").click()
    driver.find_element(By.XPATH, "//button[@data-cy='book-now-action-button']").click()
    time.sleep(5)

    driver.find_element(By.XPATH, "//input[@id='name']").send_keys(name)
    driver.find_element(By.XPATH, f"//input[@id='gender-{gender}']").click()
    driver.find_element(By.XPATH, "//input[@id='phone']").send_keys(phone)
    driver.find_element(By.XPATH, "//input[@id='email']").send_keys(email)
    driver.find_element(By.XPATH, f"//div[@value='{purpose}']").click()
    privacy_checkbox = driver.find_element(By.XPATH, "//input[@id='privacy-policy']")
    driver.execute_script("arguments[0].scrollIntoView(true);", privacy_checkbox)
    time.sleep(1)
    driver.find_element(By.XPATH, "//label[@for='privacy-policy']").click()
    driver.find_element(By.XPATH, "//button[@type='submit']").click()
