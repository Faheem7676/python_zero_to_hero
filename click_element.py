from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Setup Chrome options
options = webdriver.ChromeOptions()
options.add_argument("user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36")

# Initialize WebDriver
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)

# Increase timeout settings
driver.set_page_load_timeout(300)  # Wait up to 5 minutes

try:
    print("Opening website...")
    driver.get("https://www.gabrielny.com/")  
    driver.maximize_window()
    
    # Wait for the page to fully load
    wait = WebDriverWait(driver, 20)

    print("Hovering on 'Engagement Rings'...")
    engagement_ring = wait.until(EC.presence_of_element_located((By.XPATH, "//ul[@class='ui-menu menu-main-ul']/li[1]")))
    
    actions = ActionChains(driver)
    actions.move_to_element(engagement_ring).perform()
    
    print("Clicking 'Round' option...")
    round_element = wait.until(EC.element_to_be_clickable((By.XPATH, "//li/ul/li/a/span[text()='Round']")))
    round_element.click()

    print("Successfully clicked on 'Round'!")
    
except Exception as e:
    print("Error:", str(e))

finally:
    driver.quit()
