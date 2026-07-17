from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

driver.get("https://demoqa.com/text-box")

driver.find_element(By.ID, "userName").send_keys("Anthony")
driver.find_element(By.ID, "userEmail").send_keys("abcgmail.com")

driver.find_element(By.ID, "submit").click()

email = driver.find_element(By.ID, "userEmail")

if "field-error" in email.get_attribute("class"):
    print("Invalid email format verified")
else:
    print("Validation failed")

driver.quit()