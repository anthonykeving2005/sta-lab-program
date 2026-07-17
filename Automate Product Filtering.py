from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

driver.get("https://demo.opencart.com")

search = driver.find_element(By.NAME, "search")
search.send_keys("MacBook")

driver.find_element(By.CSS_SELECTOR, "button.btn.btn-light").click()

print("Product search completed")

driver.quit()