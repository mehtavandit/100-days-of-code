import time

from selenium import webdriver

# Note: expects Google Chrome and the appropriate ChromeDriver to be properly installed on the system
# https://chromedriver.chromium.org/downloads

LOGIN_URL = "https://www.linkedin.com/login"
# job listings to look at, includes position and location
JOBS_URL = "https://www.linkedin.com/jobs/search/?f_LF=f_AL" \
           "&keywords=python%20developer" \
           "&location=Ahmedabad%2C%20England%2C%20United%20Kingdom"

EMAIL = ************** # Enter your mail
PASSWORD = ************ # Enter your password
CONTACT_NUMBER = *********** # Enter your contact number
chrome_driver_path = "C:\Development\chromedriver.exe"
driver = webdriver.Chrome(executable_path=chrome_driver_path)

def login():
    driver.get(url=LOGIN_URL)
    time.sleep(2)
    # accept cookies
    driver.find_element_by_xpath('//*[@id="artdeco-global-alert-container"]/div[1]/section/div/div[2]/button[2]')\
        .click()
    # fill in login credentials and submit
    driver.find_element_by_id("username").send_keys(EMAIL)
    driver.find_element_by_id("password").send_keys(PASSWORD)
    driver.find_element_by_id("password").submit()


def get_job_urls():
    driver.get(url="https://www.linkedin.com/jobs/search/?f_LF=f_AL&geoId=104990346&keywords=python%20developer&location=Ahmedabad%2C%20Gujarat%2C%20India")
    time.sleep(2)
    jobs = driver.find_elements_by_class_name("job-card-container__link")
    job_url_list = []
    for job in jobs:
        job_url = job.get_attribute("href")
        if job_url.find("www.linkedin.com/jobs/view/") >= 0 and job_url not in job_url_list:
            job_url_list.append(job_url)
    return job_url_list


def apply_to_job(link):
    driver.get(url=link)
    time.sleep(2)
    driver.find_element_by_class_name("jobs-apply-button").click()
    time.sleep(1)
    button = driver.find_element_by_css_selector("footer button")
    if button.text == "Submit application":
        # fill out the phone number
        driver.find_element_by_class_name("fb-single-line-text__input").send_keys(CONTACT_NUMBER)
        # applying to random jobs automatically is really not a good idea, so instead of a button.click()...
        button.click()
    else:
        # if the application requires additional steps, skip it, but to have some feedback
        print(f"One-step application is not possible for this job.")


login()
time.sleep(3)


url_list = get_job_urls()
if len(url_list) == 0:
    print("No jobs found.\nMake sure you're logged in properly or tweak the position or location name.")


for url in url_list:
    apply_to_job(url)
    time.sleep(5)

driver.close()
