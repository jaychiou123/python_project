from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException
import time

EMAIL="jay912145@gmail.com"
PASSWORD="z1247258"
PHONE="939862682"
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
driver.get("https://www.linkedin.com/jobs/search/?currentJobId=3095017730&f_AL=true&geoId=104187078&keywords=python%20developer")

log_in = driver.find_element(By.CSS_SELECTOR, ".nav__button-secondary.btn-md.btn-secondary-emphasis")
log_in.click()
time.sleep(1)
email = driver.find_element(By.ID, "username")
email.send_keys(EMAIL)
password = driver.find_element(By.ID, "password")
password.send_keys(PASSWORD)
password.send_keys(Keys.ENTER)
time.sleep(3)

all_listings = driver.find_elements(By.CSS_SELECTOR, ".job-card-container--clickable")

for listing in all_listings:
    print("called")
    listing.click()
    time.sleep(2)

    # Try to locate the apply button, if can't locate then skip the job.
    try:
        apply_button = driver.find_element(By.CSS_SELECTOR, ".jobs-s-apply button")
        apply_button.click()
        time.sleep(5)

        # If phone field is empty, then fill your phone number.
        phone = driver.find_element(By.CLASS_NAME, "fb-single-line-text__input")
        if phone.text == "":
            phone.send_keys(PHONE)

        submit_button = driver.find_element(By.CSS_SELECTOR, "footer button")

        # If the submit_button is a "Next" button, then this is a multi-step application, so skip.
        if submit_button.get_attribute("data-control-name") == "continue_unify":
            close_button = driver.find_element(By.CLASS_NAME, "artdeco-modal__dismiss")
            close_button.click()
            time.sleep(2)
            discard_button = driver.find_elements(By.CLASS_NAME, "artdeco-modal__confirm-dialog-btn")[1]
            discard_button.click()
            print("Complex application, skipped.")
            continue
        else:
            submit_button.click()

        # Once application completed, close the pop-up window.
        time.sleep(2)
        close_button = driver.find_element(By.CLASS_NAME, "artdeco-modal__dismiss")
        close_button.click()

    # If already applied to job or job is no longer accepting applications, then skip.
    except NoSuchElementException:
        print("No application button, skipped.")
        continue
# cancel = driver.find_element(By.CSS_SELECTOR, ".artdeco-modal-overlay .mercado-match")
# cancel.click()
time.sleep(2000)