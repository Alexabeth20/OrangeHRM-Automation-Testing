from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Path to ChromeDriver
chromedriver_path = "/Users/mayergroup/Documents/Coding :Tech/QA Testing/chromedriver/chromedriver"
service = Service(chromedriver_path)

# Initialize the WebDriver
driver = webdriver.Chrome(service=service)

try:
    # Step 1: Navigate to the login page
    driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
    print("Login page opened successfully.")

    # Step 2: Enter invalid credentials
    driver.find_element(By.NAME, "username").send_keys("InvalidUser")
    driver.find_element(By.NAME, "password").send_keys("InvalidPass")
    driver.find_element(By.XPATH, "//button[@type='submit']").click()
    print("Entered invalid credentials and clicked login.")

    # Step 3: Wait for the error message to appear
    wait = WebDriverWait(driver, 20)  # Increased wait time
    try:
        # Primary XPath
        error_message = wait.until(EC.visibility_of_element_located((By.XPATH, "//div[contains(@class, 'oxd-alert-content') and contains(text(), 'Invalid credentials')]")))
    except:
        print("Primary XPath failed. Trying broader XPath...")
        # Broader XPath as fallback
        error_message = wait.until(EC.visibility_of_element_located((By.XPATH, "//div[contains(@class, 'oxd-alert-content')]")))

    # Debugging: Print all matching elements
    elements = driver.find_elements(By.XPATH, "//div[contains(@class, 'oxd-alert-content')]")
    for element in elements:
        print(f"Element text: {element.text}")

    # Validate the error message
    assert "Invalid credentials" in error_message.text, "Error message text does not match."
    print("Test Passed: Error message displayed for invalid login.")

except AssertionError as e:
    print(f"Test Failed: {e}")

finally:
    # Close the browser
    driver.quit()
    