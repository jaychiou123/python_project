from selenium import webdriver
import undetected_chromedriver as uc
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import ElementClickInterceptedException, NoSuchElementException
import time
EMAIL= MY_EMAIL
PASSWORD= MY_PASSWORD

driver = uc.Chrome(use_subprocess=True)
driver.get("https://tinder.com/")
time.sleep(5)
login = driver.find_element(By.XPATH, '//*[@id="s2097736098"]/div/div[1]/div/main/div[1]/div/div/div/div/header/div/div[2]/div[2]/a')
login.click()
time.sleep(3)
fb = driver.find_element(By.XPATH, '//*[@id="s369355022"]/div/div/div[1]/div/div/div[3]/span/div[2]/button')
fb.click()
time.sleep(5)

## switching to login handler
base_window = driver.window_handles[0]
fb_login_window = driver.window_handles[1]
driver.switch_to.window(fb_login_window)
print(driver.title)

## log in
email = driver.find_element(By.XPATH, '//*[@id="email"]')
email.send_keys(EMAIL)
password = driver.find_element(By.XPATH, '//*[@id="pass"]')
password.send_keys(PASSWORD)
password.send_keys(Keys.ENTER)
time.sleep(2)
driver.switch_to.window(base_window)
print(driver.title)

## enable cookies and notification
time.sleep(5)
allow_location_button = driver.find_element(By.XPATH, '//*[@id="modal-manager"]/div/div/div/div/div[3]/button[1]')
allow_location_button.click()
notifications_button = driver.find_element(By.XPATH, '//*[@id="modal-manager"]/div/div/div/div/div[3]/button[2]')
notifications_button.click()
cookies = driver.find_element(By.XPATH, '//*[@id="content"]/div/div[2]/div/div/div[1]/button')
cookies.click()

for n in range(100):
    time.sleep(1)
    try:
        print("called")
        like_button = driver.find_element(By.XPATH, '//*[@id="content"]/div/div[1]/div/main/div[1]/div/div/div[1]/div/div[2]/div[4]/button')
        like_button.click()
    except ElementClickInterceptedException:
        try:
            match_popup = driver.find_element(By.CSS_SELECTOR, ".itsAMatch a")
            match_popup.click()
        except NoSuchElementException:
            time.sleep(2)

driver.quit()