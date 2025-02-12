from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import time

# Initialize WebDriver
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

# Open multiple tabs
driver.get("https://www.google.com")
time.sleep(2)
driver.maximize_window()
driver.execute_script("window.open('https://www.gabrielny.com');") # opens last tab
time.sleep(2)
driver.execute_script("window.open('https://www.bing.com');")
time.sleep(2)
driver.execute_script("window.open('https://www.yahoo.com');")  # Opens 3rd tab
time.sleep(2)


# Get all tab handles
tabs = driver.window_handles

# Switch to the first tab and close it
driver.switch_to.window(tabs[0])
time.sleep(4)
driver.close()

# Switch to the second tab (now the first one after closing)
driver.switch_to.window(tabs[1])
# Perform further actions if needed
print("First tab closed successfully!")

# Switch to the last tab and close it
driver.switch_to.window(tabs[-1])
driver.close()

# Switch back to the previous tab
driver.switch_to.window(tabs[-2])

# Perform further actions if needed
print("Last tab closed successfully!")

# Keep browser open for verification (optional)
import time
time.sleep(5)

# Close browser
driver.quit()
