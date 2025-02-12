from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
import time

# Initialize WebDriver
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

# Open a website
driver.get("https://www.example.com")
driver.maximize_window()
currentURL=driver.current_url
print("Current URL:",currentURL)

# assert 'https://www.example.com'==currentURL,"URLs are different!"
time.sleep(2)  # Wait for elements to load
