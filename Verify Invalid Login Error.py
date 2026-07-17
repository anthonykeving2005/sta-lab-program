from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

driver.get("https://www.saucedemo.com")

driver.find_element(By.ID, "user-name").send_keys("wronguser")
driver.find_element(By.ID, "password").send_keys("wrongpassword")
driver.find_element(By.ID, "login-button").click()

error = driver.find_element(By.CSS_SELECTOR, "h3").text
print(error)

driver.quit()