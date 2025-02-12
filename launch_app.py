from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options

# Set up Chrome options
chrome_options = Options()
chrome_options.set_capability('goog:loggingPrefs', {'browser': 'ALL'})

# Initialize the WebDriver
service = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=service, options=chrome_options)

# Navigate to the web application
driver.get("https://demo.competethemes.com/")

try:
    # Define a wait time (e.g., 20 seconds)
    wait = WebDriverWait(driver, 120)

    # Wait until the element is visible
    element = wait.until(EC.visibility_of_element_located((By.XPATH, "//li[@id='menu-item-341']")))

    # Wait until the element is clickable
    clickable_element = wait.until(EC.element_to_be_clickable((By.XPATH, "//li[@id='menu-item-341']")))

    # Perform actions on the element
    clickable_element.click()
    print("Element clicked successfully.")

    # Wait until the element is no longer visible
    wait.until(EC.invisibility_of_element_located((By.XPATH, "//div[@class='button']/a")))
    print("Element is no longer visible.")

except TimeoutException:
    print("The element was not found or did not become invisible within the given time.")

finally:
    # Close the browser
    driver.quit()
