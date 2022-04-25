from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.common.exceptions import ElementClickInterceptedException, NoSuchElementException
import time

email = "****************" #Enter your email
password = "***********"   #Enter your password

chrome_driver_path = "C:\Development\chromedriver.exe"
driver = webdriver.Chrome(executable_path=chrome_driver_path)

driver.get("http://www.tinder.com")


def login():
    time.sleep(5)
    driver.find_element(By.XPATH,
                        '/html/body/div[1]/div/div[1]/div/main/div[1]/div/div/div/div/header/div/div[2]/div[2]/a').click()
    time.sleep(5)
    driver.find_element(By.XPATH, '/html/body/div[2]/div/div/div[1]/div/div/div[3]/span/div[2]/button').click()
    time.sleep(5)
    base_window = driver.window_handles[0]
    facebook_window = driver.window_handles[1]
    driver.switch_to.window(facebook_window)
    print(driver.title)
    email_input = driver.find_element(By.XPATH, "/html/body/div/div[2]/div[1]/form/div/div[1]/div/input")
    password_input = driver.find_element(By.XPATH, '/html/body/div/div[2]/div[1]/form/div/div[2]/div/input')
    email_input.send_keys(email)
    password_input.send_keys(password)
    driver.find_element(By.XPATH, '/html/body/div/div[2]/div[1]/form/div/div[3]/label[2]').click()
    driver.switch_to.window(base_window)
    print(driver.title)
    time.sleep(5)


def remove_pops():
    driver.find_element(By.XPATH, '/html/body/div[2]/div/div/div/div/div[3]/button[1]').click()
    time.sleep(5)
    driver.find_element(By.XPATH, '/html/body/div[2]/div/div/div/div/div[3]/button[2]').click()
    driver.find_element(By.XPATH, '/html/body/div[1]/div/div[2]/div/div/div[1]/div[1]/button').click()


def main_function():
    for i in range(100):
        time.sleep(2)

        try:
            driver.find_element(By.XPATH, '/html/body/div[1]/div/div[1]/div/main/div[1]/div/div/div[1]/div[1]/div/div['
                                          '4]/div/div[4]/button').click()
        except NoSuchElementException:
            time.sleep(2)


login()
remove_pops()

for n in range(100):

    # Add a 1 second delay between likes.
    time.sleep(1)

    try:
        print("called")
        like_button = driver.find_element(By.XPATH,
                                          '/html/body/div[1]/div/div[1]/div/main/div[1]/div/div/div[1]/div[1]/div/div[4]/div/div[4]/button')
        like_button.click()

    # Catches the cases where there is a "Matched" pop-up in front of the "Like" button:
    except ElementClickInterceptedException:
        try:
            match_popup = driver.find_element_by_css_selector(".itsAMatch a")
            match_popup.click()

        # Catches the cases where the "Like" button has not yet loaded, so wait 2 seconds before retrying.
        except NoSuchElementException:
            time.sleep(2)

driver.quit()
