import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager

# Setup fixture for WebDriver
@pytest.fixture
def driver():
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    driver.maximize_window()
    yield driver
    driver.quit()

# Helper function to perform login
def login(driver, username, password):
    driver.get("https://allenplus.allen.ac.in/login")  # Replace with actual URL
    wait = WebDriverWait(driver, 10)
    
    # Locate elements and enter credentials
    username_field = wait.until(EC.presence_of_element_located((By.XPATH, "//input[@name='user']")))
    password_field = driver.find_element(By.XPATH, "//input[@name='pass']")
    login_button = driver.find_element(By.XPATH, "//button[@type='submit']")
    
    username_field.send_keys(username)
    password_field.send_keys(password)
    login_button.click()

# Test cases
def test_valid_login(driver):
    login(driver, "dumst20", "dstd#123")
    assert "Homework" in driver.page_source, "Login failed: Homework button not found"

def test_invalid_username(driver):
    login(driver, "invalidUser", "dstd#123")
    assert "Invalid username" in driver.page_source, "Error message not displayed"

def test_invalid_password(driver):
    login(driver, "dumst20", "wrongpass")
    assert "Incorrect password" in driver.page_source, "Error message not displayed"

def test_empty_credentials(driver):
    login(driver, "", "")
    assert "Please enter username and password" in driver.page_source, "Error message not displayed"

def test_sql_injection(driver):
    login(driver, "admin' OR 1=1 --", "randompass")
    assert "Invalid username" in driver.page_source, "SQL injection vulnerability found"

def test_xss_attack(driver):
    login(driver, "<script>alert('XSS')</script>", "password")
    assert "<script>" not in driver.page_source, "XSS vulnerability found"

def test_case_sensitivity(driver):
    login(driver, "DumSt20", "dstd#123")
    assert "Invalid username" in driver.page_source, "Case sensitivity issue in username"

def test_login_without_captcha(driver):
    login(driver, "dumst20", "dstd#123")
    assert "CAPTCHA required" in driver.page_source, "Captcha validation missing"

