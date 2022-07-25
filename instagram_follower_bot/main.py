from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import undetected_chromedriver as uc
from selenium.common.exceptions import ElementClickInterceptedException
import time

SIMILAR_ACCOUNT="toptennistraining"
USERNAME=MY_USERNAME
PASSWORD=MY_PASSWORD

class InstaFollower:

    def __init__(self):
        self.driver = uc.Chrome(use_subprocess=True)
        self.loginurl = "https://www.instagram.com/accounts/login/"
        self.targeturl = f"https://www.instagram.com/{SIMILAR_ACCOUNT}/"
        self.target_follower_url = self.targeturl + "followers/"

    def login(self):
        self.driver.get(self.loginurl)
        time.sleep(2)
        username = self.driver.find_element(By.XPATH, '//*[@id="loginForm"]/div/div[1]/div/label/input')
        username.send_keys(USERNAME)
        password = self.driver.find_element(By.XPATH, '//*[@id="loginForm"]/div/div[2]/div/label/input')
        password.send_keys(PASSWORD)
        password.send_keys(Keys.ENTER)
        time.sleep(5)

    def find_followers(self):
        self.driver.get(self.target_follower_url)
        time.sleep(5)
        element_popup = self.driver.find_element(By.XPATH, '/html/body/div[1]/div/div/div/div[2]/div/div/div[1]/div/div[2]/div/div/div/div/div/div/div/div[2]')
        for i in range(10):
            self.driver.execute_script("arguments[0].scrollTop = arguments[0].scrollHeight", element_popup)
            time.sleep(2)

    def follow(self):
        all_buttons = self.driver.find_elements(By.CSS_SELECTOR, "li button")
        for button in all_buttons:
            try:
                button.click()
                time.sleep(1)
            except ElementClickInterceptedException:
                cancel_button = self.driver.find_element(By.XPATH, '/html/body/div[5]/div/div/div/div[3]/button[2]')
                cancel_button.click()


ig_bot = InstaFollower()
ig_bot.login()
ig_bot.find_followers()
ig_bot.follow()