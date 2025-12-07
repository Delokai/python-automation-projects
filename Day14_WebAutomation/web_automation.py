from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
from time import sleep

driver = webdriver.Chrome()

driver.get("https://www.google.com")

# Wait until the search box is interactable
search_box = WebDriverWait(driver, 10).until(
    EC.element_to_be_clickable((By.NAME, "q"))
)

search_box.send_keys("Python automation")
search_box.submit()

sleep(5)
driver.quit()
