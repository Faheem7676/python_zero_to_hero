from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
import time
import json

# Configure ChromeOptions for CDP
chrome_options = Options()
chrome_options.add_experimental_option("goog:loggingPrefs", {"performance": "ALL"})

# Start Chrome WebDriver
service = Service("")  # Update with your actual ChromeDriver path
driver = webdriver.Chrome(service=service, options=chrome_options)

# Navigate to login page
driver.get("https://allenplus.allen.ac.in/login")  # Replace with your actual login page

# Enter login credentials
driver.find_element(By.XPATH, "(//input[@name='user'])[1]").send_keys("dumst20")
driver.find_element(By.XPATH, "//input[@name='pass']").send_keys("dstd#123")
driver.find_element(By.XPATH,"//input[@id='reg-code']").send_keys("susr")
driver.find_element(By.XPATH, "//button[@id='submit']").click()  # Update with the actual login button selector

time.sleep(5)  # Wait for API requests to process

# Capture network logs
logs = driver.get_log("performance")

# Analyze API calls
for log in logs:
    try:
        log_json = json.loads(log["message"])["message"]
        
        # Check for network responses
        if log_json["method"] == "Network.responseReceived":
            response_url = log_json["params"]["response"]["url"]
            status_code = log_json["params"]["response"]["status"]
            
            print(f"API URL: {response_url} | Status Code: {status_code}")

            # Check if any API failed (status code >= 400)
            if status_code >= 400:
                print(f"❌ API Failed: {response_url} | Status: {status_code}")
    
    except Exception as e:
        print(f"Error parsing log: {e}")

# Close the browser
driver.quit()


# locators
	

	# _email_field="(//input[@name='user'])[1]"
	# _password_field="//input[@name='pass']"
	# _captchatext="//input[@id='reg-code']"
	# _loginbutton="//button[@id='submit']"
	# _accessbutton="//a[text()=' Access Request']"
	# _sessionpopup="ng-binding"
	# _popupdone="button"
	# _userprofile="//img[@class='rounded-circle ng-star-inserted']"
	# _logout="//a[text()=' Logout']"
	# _accesscancelbutton="//button[text()='Cancel']"
	# _selectsessionpop="//p[@id='5']"
	# _submitsessionpop="//button[text()='Select']"