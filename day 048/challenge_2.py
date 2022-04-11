from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By

chrome_driver_path = "C:\Development\chromedriver.exe"
driver = webdriver.Chrome(executable_path=chrome_driver_path)

driver.get("http://secure-retreat-92358.herokuapp.com/")

# digit = driver.find_element(By.CSS_SELECTOR, "#articlecount a")
# digit.click()
#
# all_portals = driver.find_element(By.LINK_TEXT, "All portals")
# all_portals.click()
#
# search = driver.find_element(By.NAME, "search")
# search.send_keys("Python")
# search.send_keys(Keys.ENTER)

fname = driver.find_element(By.NAME, "fName")
lname = driver.find_element(By.NAME, "lName")
email = driver.find_element(By.NAME, "email")
button = driver.find_element(By.CSS_SELECTOR, ".btn-lg")
fname.send_keys("Vandit")
lname.send_keys("Mehta")
email.send_keys("fasfgg@gmail.com")
button.click()
