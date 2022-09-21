from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time


def convert_int(a_string):
    sep = a_string.split(",")[::-1]
    total = 0
    for i in sep:
        total += int(i) * pow(1000, sep.index(i))
    return total

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
driver.get("http://orteil.dashnet.org/experiments/cookie/")
cookie = driver.find_element(By.ID, "cookie")
time_now=0
while 1:
    if time.time()-time_now >= 5.0:
        money = convert_int(driver.find_element(By.ID, "money").text)
        tools = driver.find_elements(By.CSS_SELECTOR, "#store div b")
        list_affordable = [(i.text.split()[0], convert_int(i.text.split()[-1])) for i in tools[:len(tools)-1] if convert_int(i.text.split()[-1]) <= money]
        if len(list_affordable) != 0:
            item_to_buy = driver.find_element(By.ID, f"buy{list_affordable[-1][0]}")
            item_to_buy.click()
        time_now = time.time()
    cookie.click()
time.sleep(200)

# driver.quit()
