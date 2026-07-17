from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import time

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

driver.get("https://automationexercise.com")

driver.find_element(By.LINK_TEXT, "Signup / Login").click()

driver.find_element(By.NAME, "name").send_keys("Anthony Kevin")
driver.find_element(By.XPATH, "//input[@data-qa='signup-email']").send_keys("anthony123456@gmail.com")

driver.find_element(By.XPATH, "//button[@data-qa='signup-button']").click()

print("Registration page opened successfully")

time.sleep(5)

driver.quit()