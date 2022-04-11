import time

from selenium import webdriver
from selenium.webdriver.common.by import By

# Note: expects Google Chrome and the appropriate ChromeDriver to be properly installed on the system
# https://chromedriver.chromium.org/downloads

TIMEOUT = 15000
CHECK_INTERVAL = 5


def buy_upgrade():
    """Purchases the most expensive available upgrade."""
    # get current number of cookies
    raw_cookies=driver.find_element(By.ID, "money").text
    # remove the possible period
    cookies = int(raw_cookies.replace(",", ""))

    raw_prices = driver.find_element(By.CSS_SELECTOR, "#store b")
    prices = [int(price.text.split("-")[1].strip().replace(",", "")) for price in raw_prices if price.text != ""]

    upgrades = {}
    for n in range(len(prices)):
        upgrades[prices[n]] = item_ids[n]

    # find purchasable upgrades
    purchasable_upgrades = {}
    for upgrade_cost, upgrade_id in upgrades.items():
        if cookies > upgrade_cost:
            purchasable_upgrades[upgrade_cost] = upgrade_id

    # click on the most expensive purchasable upgrade
    driver.find_element(By.ID, purchasable_upgrades[max(purchasable_upgrades)]).click()


# executable_path="..." argument is not necessary if the webdriver executable is placed in a folder included in PATH
# e.g. in C:\Windows
chrome_driver_path = "C:\Development\chromedriver.exe"
driver = webdriver.Chrome(executable_path=chrome_driver_path)
driver.get("http://orteil.dashnet.org/experiments/cookie/")
cookie = driver.find_element(By.ID, "cookie")

# get store items
item_list = driver.find_elements(By.CSS_SELECTOR, "#store div")
item_ids = [item.get_attribute("id") for item in item_list]

# set timers
start_time = time.time()
end_time = start_time + TIMEOUT
check_time = start_time + CHECK_INTERVAL

while time.time() < end_time:
    # click with each iteration
    cookie.click()
    # check for upgrades after the set about of time
    if time.time() > check_time:
        buy_upgrade()
        # time for the next the next check
        check_time += CHECK_INTERVAL

# print the cookie per second value at the end
cps = driver.find_element(By.ID,"cps").text
print(f"Exited after {TIMEOUT} seconds with a score of {cps.split(' : ')[1]} cookies per second.")

# close the browser window
driver.close()
