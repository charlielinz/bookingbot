from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.action_chains import ActionChains
from selenium.common.exceptions import NoSuchElementException
import pathlib
import time
import json

with open("inline.json") as jsonfile:
    inline_url = json.load(jsonfile)

orders = [
    {
        "restaurant": "fermi",
        "persons": {"adults": "7", "kids": "2"},
        "date": "09-20",
        "time": "18:00",
        "name": "Charlie",
        "gender": "male",  # female, male, none
        "phone": "0983097997",
        "email": "ilovealinlin@gmail.com",
        "purpose": "慶生",  # 慶生 約會 週年慶 家庭用餐 朋友聚餐 商務聚餐
    }
]

base_dir = pathlib.Path(__file__).resolve().parent
service = Service(base_dir / "chromedriver")
driver = webdriver.Chrome(service=service)
actions = ActionChains(driver)
index = 0


for order in orders:
    # order infos
    restaurant = order["restaurant"]
    adults = order["persons"]["adults"]
    kids = order["persons"]["kids"]
    date = order["date"]
    time_ = order["time"].replace(":", "-")
    name = order["name"]
    gender = order["gender"]
    phone = order["phone"]
    email = order["email"]
    purpose = order["purpose"]

    # get to inline page
    driver.execute_script(f"window.open('{inline_url[restaurant]}', 'tab{index}')")
    driver.switch_to.window(f"tab{index}")
    time.sleep(5)

    # get available seats
    try:
        kid_pickers = driver.find_elements(By.XPATH, "//select[@id='kid-picker']/option")
        available_kids = []
    except NoSuchElementException:
        break
    adult_pickers = driver.find_elements(By.XPATH, "//select[@id='adult-picker']/option")
    available_adults = []
    for adult_picker in adult_pickers:
        if not adult_picker.get_dom_attribute("disabled"):
            available_adults.append(adult_picker.get_dom_attribute("value"))
    for kid_picker in kid_pickers:
        if not kid_picker.get_dom_attribute("disabled"):
            available_kids.append(kid_picker.get_dom_attribute("value"))
    print(available_adults, available_kids)

    # first order page
    if kids == "0":
        print("You enter wrong kids number.")
    elif (kids != 0) & (kids in available_kids):
        driver.find_element(By.XPATH, f"//select[@id='kid-picker']/option[@value='{kids}']").click()
        print(f"there are seats for {kids} kids")
    else:
        print(f"not enough seats for {kids} kids")
    if adults == "0":
        print("You enter wrong adults number.")
    elif adults in available_adults:
        driver.find_element(By.XPATH, f"//select[@id='adult-picker']/option[@value='{adults}']").click()
        print(f"there are seats for {adults} adults")
    else:
        print(f"not enough seats for {adults} adults")
    # date_picker = driver.find_element(By.XPATH, "//div[@id='date-picker']")
    # driver.execute_script("arguments[0].scrollIntoView(true);", date_picker)
    # time.sleep(0.5)
    # driver.execute_script("arguments[0].scrollIntoView(true);", date_picker)
    # time.sleep(1)
    # driver.find_element(By.XPATH, "//div[@id='date-picker']").click()
    # time.sleep(0.5)
    # driver.find_element(By.XPATH, f"//div[@data-date='2022-{date}']").click()
    # time.sleep(1.5)
    # driver.find_element(By.CLASS_NAME, f"time-slot-{time_}").click()
    # driver.find_element(By.XPATH, "//button[@data-cy='book-now-action-button']").click()
    # time.sleep(5)

    # # second order page
    # driver.find_element(By.XPATH, "//input[@id='name']").send_keys(name)
    # driver.find_element(By.XPATH, f"//input[@id='gender-{gender}']").click()
    # driver.find_element(By.XPATH, "//input[@id='phone']").send_keys(phone)
    # driver.find_element(By.XPATH, "//input[@id='email']").send_keys(email)
    # driver.find_element(By.XPATH, f"//div[@value='{purpose}']").click()
    # privacy_checkbox = driver.find_element(By.XPATH, "//input[@id='privacy-policy']")
    # driver.execute_script("arguments[0].scrollIntoView(true);", privacy_checkbox)
    # time.sleep(1)
    # driver.find_element(By.XPATH, "//label[@for='privacy-policy']").click()
    # driver.find_element(By.XPATH, "//button[@type='submit']").click()

    index += 1
