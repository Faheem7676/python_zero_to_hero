import csv
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager
import time

# Setup WebDriver
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
driver.maximize_window()

# Read credentials from CSV
input_file = "login_data.csv"
output_data = []

with open(input_file, "r") as file:
    reader = csv.reader(file)
    header = next(reader)  # Read header
    output_data.append(header + ["Status"])  # Add "Status" column

    for row in reader:
        username, password = row[0], row[1]

        try:
            # Open the website
            driver.get("https://allenplus.allen.ac.in/login")  # Replace with actual login page
            
            # Wait for elements to load
            wait = WebDriverWait(driver, 10)
            
            # Locate and input credentials
            username_input = wait.until(EC.presence_of_element_located((By.XPATH, "//form/label/input[@name='user']")))
            password_input = driver.find_element(By.XPATH, "//form/label/input[@name='pass']")

            username_input.clear()
            password_input.clear()
            username_input.send_keys(username)
            password_input.send_keys(password)
            
            # Handle captcha manually
            captcha = driver.find_element(By.XPATH, "//div/label/input[@id='reg-code']")
            captcha.click()
            time.sleep(10)  # Give time for manual captcha input
            
            # Click login button
            login_button = driver.find_element(By.XPATH, "//button[@type='submit']")
            login_button.click()
            time.sleep(4)
            
            profile_button=driver.find_element(By.XPATH,"//div[@class='show']")
            profile_button.click()
            
            logout_button=driver.find_element(By.XPATH,"//div/a[@class='dropdown-item d-flex align-items-center'][2]")
            login_button.click()
            login_button.click()

            # Verify login success
            try:
                wait.until(EC.presence_of_element_located((By.XPATH, "//nav[@class='no-allen']/ul/li[@id='studytour']")))
                print(f"✅ Login successful for: {username}")
                output_data.append(row + ["Pass"])
            except:
                print(f"❌ Login failed for: {username}")
                output_data.append(row + ["Fail"])

        except Exception as e:
            print(f"⚠️ Error logging in with {username}: {str(e)}")
            output_data.append(row + ["Error"])

# Write results back to CSV
output_file = "login_results.csv"  # Save as a new file to keep original
with open(output_file, "w", newline="") as file:
    writer = csv.writer(file)
    writer.writerows(output_data)

print(f"✅ Results saved to {output_file}")

# Close browser
driver.quit()
