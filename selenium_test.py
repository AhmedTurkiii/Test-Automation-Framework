from selenium import webdriver
import time
from selenium.webdriver.common.by import By


driver = webdriver.Chrome()
driver.get("http://www.python.org")
print(driver.title)

search_bar = driver.find_element(By.ID, "id-search-field")
search_bar.send_keys("asyncio")

time.sleep(2)
driver.quit()