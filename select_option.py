from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

# Setup WebDriver
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
driver.maximize_window()

def login(driver, username, password):
    """Logs in to the website."""
    driver.get("https://allenplus.allen.ac.in/login")  # Replace with the actual login page URL
    wait = WebDriverWait(driver, 10)

    user_field = wait.until(EC.presence_of_element_located((By.XPATH, "//form/label/input[@name='user']")))
    pass_field = driver.find_element(By.XPATH, "//form/label/input[@name='pass']")
    
    user_field.send_keys(username)
    pass_field.send_keys(password)

    captcha = driver.find_element(By.XPATH, "//div/label/input[@id='reg-code']")
    captcha.click()
    time.sleep(10)  # Allow time for CAPTCHA input

    login_button = driver.find_element(By.XPATH, "//button[@type='submit']")
    login_button.click()

def click_element(wait, xpath, element_name="Element"):
    """Clicks an element if found."""
    try:
        element = wait.until(EC.element_to_be_clickable((By.XPATH, xpath)))
        element.click()
        print(f"✅ {element_name} clicked successfully.")
        return True
    except Exception as e:
        print(f"❌ Failed to click {element_name}: {str(e)}")
        return False

def select_my_asset_option(driver, option_name):
    """Clicks on a given option under 'My Assets'."""
    wait = WebDriverWait(driver, 10)

    # Click 'My Assets'
    click_element(wait, "//span[normalize-space()='My Assets']", "My Assets")

    # Click the specified option (My Notes or My Homework)
    option_xpath = f"//span[normalize-space()='{option_name}']"
    if click_element(wait, option_xpath, option_name):
        print(f"✅ Successfully clicked on '{option_name}'.")
    else:
        print(f"❌ '{option_name}' not found or not clickable.")

# Run the script
try:
    login(driver, "dumst20", "dstd#123")  # Replace with actual credentials
    time.sleep(3)  # Allow time for login
    select_my_asset_option(driver, "My Notes")  # Change to "My Notes" if needed
finally:
    driver.quit()
