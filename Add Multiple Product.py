from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

wait = WebDriverWait(driver, 10)

driver.get("https://www.saucedemo.com")

driver.find_element(By.ID,"user-name").send_keys("standard_user")
driver.find_element(By.ID,"password").send_keys("secret_sauce")
driver.find_element(By.ID,"login-button").click()

# Wait for the product list to finish rendering before clicking items.
wait.until(EC.presence_of_all_elements_located((By.CSS_SELECTOR, "button.btn_inventory")))

# Add first two products
buttons = driver.find_elements(By.CSS_SELECTOR, "button.btn_inventory")

if len(buttons) < 2:
	raise AssertionError(f"Expected at least 2 add-to-cart buttons, found {len(buttons)}")

buttons[0].click()
buttons[1].click()

driver.find_element(By.CLASS_NAME,"shopping_cart_link").click()

cart_items = driver.find_elements(By.CLASS_NAME,"cart_item")

assert len(cart_items) == 2

print("Two products added successfully!")

driver.quit()