from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

driver.maximize_window()
driver.get("https://demoqa.com/text-box")

driver.find_element(By.ID, "userName").send_keys("Anthony Kevin")
driver.find_element(By.ID, "userEmail").send_keys("anthony@gmail.com")
driver.find_element(By.ID, "currentAddress").send_keys("Bangalore")
driver.find_element(By.ID, "permanentAddress").send_keys("Bangalore")

driver.find_element(By.ID, "submit").click()

print("Contact form submitted successfully")

driver.quit()