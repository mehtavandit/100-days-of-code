from selenium import webdriver
import time

from selenium.webdriver.common.by import By

chrome_driver_path = "C:\Development\chromedriver.exe"
driver = webdriver.Chrome(executable_path=chrome_driver_path)

driver.get("https://www.python.org/")


times = driver.find_elements(By.CSS_SELECTOR, ".event-widget time")
names = driver.find_elements(By.CSS_SELECTOR, ".event-widget li a")
upcoming_events = {}

for n in range(len(times)):
    upcoming_events[n] = {
        "time" : times[n].text,
        "name" : names[n].text
    }

print(upcoming_events)
