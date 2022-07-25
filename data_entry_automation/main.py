import time
from bs4 import BeautifulSoup
import requests
import json
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import undetected_chromedriver as uc

SHEET="https://docs.google.com/forms/d/e/1FAIpQLScDqEg3kHkP4fS88Q8HNMt7IJoKrI3LQMXPYL1whoBmXaBMcg/viewform?usp=sf_link"
headers = {
	"User-Agent" : "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/104.0.0.0 Safari/537.36",
	"Accept-Language":"zh-TW,zh;q=0.9,en-US;q=0.8,en;q=0.7,zh-CN;q=0.6"
}
url = "https://www.zillow.com/san-francisco-ca/rentals/1-_beds/?searchQueryState=%7B%22pagination%22%3A%7B%7D%2C%22usersSearchTerm%22%3A%22San%20Francisco%2C%20CA%22%2C%22mapBounds%22%3A%7B%22west%22%3A-122.56825534228516%2C%22east%22%3A-122.29840365771484%2C%22south%22%3A37.6956022862589%2C%22north%22%3A37.85489581746633%7D%2C%22regionSelection%22%3A%5B%7B%22regionId%22%3A20330%2C%22regionType%22%3A6%7D%5D%2C%22isMapVisible%22%3Atrue%2C%22filterState%22%3A%7B%22price%22%3A%7B%22min%22%3A0%2C%22max%22%3A450506%7D%2C%22mp%22%3A%7B%22min%22%3A0%2C%22max%22%3A2000%7D%2C%22beds%22%3A%7B%22min%22%3A1%7D%2C%22fsba%22%3A%7B%22value%22%3Afalse%7D%2C%22fsbo%22%3A%7B%22value%22%3Afalse%7D%2C%22nc%22%3A%7B%22value%22%3Afalse%7D%2C%22fore%22%3A%7B%22value%22%3Afalse%7D%2C%22cmsn%22%3A%7B%22value%22%3Afalse%7D%2C%22auc%22%3A%7B%22value%22%3Afalse%7D%2C%22fr%22%3A%7B%22value%22%3Atrue%7D%2C%22ah%22%3A%7B%22value%22%3Atrue%7D%7D%2C%22isListVisible%22%3Atrue%2C%22mapZoom%22%3A12%7D"
response = requests.get(url, headers=headers)
zillow_web = response.text
soup = BeautifulSoup(zillow_web, "html.parser")
data = soup.select_one("script[data-zrr-shared-data-key]").string.strip("!<>-")
data = json.loads(data)
link_list = [result["imgSrc"] for result in data["cat1"]["searchResults"]["listResults"]]
price_list = []
addresses_list = [result["address"] for result in data["cat1"]["searchResults"]["listResults"]]
for result in data["cat1"]["searchResults"]["listResults"]:
    try:
        price = result["units"][0]["price"]
    except KeyError:
        price = result["price"]
    price_list.append(price)
#---------------------------------------------------------------------------
## fill the form
driver = uc.Chrome(use_subprocess=True)
for i in range(len(price_list)):
    driver.get(SHEET)
    address = driver.find_element(By.XPATH, '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[1]/div/div/div[2]/div/div[1]/div/div[1]/input')
    prices = driver.find_element(By.XPATH, '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[2]/div/div/div[2]/div/div[1]/div/div[1]/input')
    links = driver.find_element(By.XPATH, '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[3]/div/div/div[2]/div/div[1]/div/div[1]/input')
    print(address)
    address.send_keys(addresses_list[i])
    prices.send_keys(price_list[i])
    links.send_keys(link_list[i])
    button = driver.find_element(By.CSS_SELECTOR, "div[role=button]")
    button.click()
    time.sleep(1)