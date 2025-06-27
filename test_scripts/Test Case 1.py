from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
import time

# Path to ChromeDriver
chromedriver_path = "/Users/mayergroup/Documents/Coding :Tech/QA Testing/chromedriver/chromedriver"
service = Service(chromedriver_path)

# Initialize the WebDriver
driver = webdriver.Chrome(service=service)

try:
    # Step 1: Navigate to the login page
    driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
    print("Login page opened successfully.")

    # Step 2: Enter valid credentials
    driver.find_element(By.NAME, "username").send_keys("Admin")
    driver.find_element(By.NAME, "password").send_keys("admin123")
    driver.find_element(By.XPATH, "//button[@type='submit']").click()
    print("Entered valid credentials and clicked login.")

    # Step 3: Validate successful login
    time.sleep(3)
    assert "dashboard" in driver.current_url.lower(), "Login failed or incorrect page loaded"
    print("Test Passed: Valid login successful and dashboard loaded.")

    # Step 4: Log out
    print("Logging out...")
    driver.find_element(By.CSS_SELECTOR, ".oxd-userdropdown-tab").click()
    time.sleep(1)
    driver.find_element(By.XPATH, "//a[text()='Logout']").click()
    print("Logged out successfully.")

finally:
    # Close the browser
    driver.quit()