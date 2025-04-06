from selenium import webdriver
import time
from selenium.webdriver.common.by import By


driver = webdriver.Chrome()
driver.get("http://www.python.org")
print(driver.title)

search_bar = driver.find_element(By.ID, "id-search-field")
go_button = driver.find_element(By.NAME, "submit")
time.sleep(2)

search_bar.send_keys("asyncio")
go_button.click()
time.sleep(2)

driver.quit()

