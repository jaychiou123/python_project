from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

driver.get("https://www.python.org/")
event_dict = {}
event_time_list=[]
event_name_list=[]
for i in range(1, 6):
    event_time= driver.find_element(By.XPATH, f'//*[@id="content"]/div/section/div[2]/div[2]/div/ul/li[{i}]/time').text
    event_name= driver.find_element(By.XPATH, f'//*[@id="content"]/div/section/div[2]/div[2]/div/ul/li[{i}]/a').text
    event_dict[i-1]={
        "time": event_time,
        "name": event_name
    }
print(event_dict)

# driver.quit()            ## shut down all tabs