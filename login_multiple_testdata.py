import csv
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager
import time
import pdb

# Setup WebDriver
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
driver.maximize_window()
#pdb.set_trace()

# Read credentials from CSV
input_file = "login_data.csv"
output_file = "login_results.csv"
output_data = []

with open(input_file, "r") as file:
    reader = csv.reader(file)
    header = next(reader)  # Read header
    output_data.append(header + ["Status"])  # Add "Status" column

    for row in reader:
        username, password = row[0], row[1]

        try:
            # Open the login page
            driver.get("https://allenplus.allen.ac.in/login")
            
            wait = WebDriverWait(driver, 10)
            
            # Locate input fields
            username_input = wait.until(EC.presence_of_element_located((By.XPATH, "//form/label/input[@name='user']")))
            password_input = driver.find_element(By.XPATH, "//form/label/input[@name='pass']")

            username_input.clear()
            password_input.clear()
            username_input.send_keys(username)
            password_input.send_keys(password)
            
            # Handle captcha manually
            input("🔵 Please enter the CAPTCHA manually and press Enter to continue...")

            # Click login button
            login_button = driver.find_element(By.XPATH, "//button[@type='submit']")
            login_button.click()
            time.sleep(2)
            print("click login button")

            # Verify login success
            try:
                wait.until(EC.presence_of_element_located((By.XPATH, "//nav[@class='no-allen']/ul/li[@id='studytour']")))
                print(f"✅ Login successful for: {username}")
                output_data.append(row + ["Pass"])
                print("Login Successfull for first time")

                # Logout process
                try:
                    profile_button = wait.until(EC.element_to_be_clickable((By.XPATH, "//div[@class='show']")))
                    profile_button.click()
                    time.sleep(2)

                    logout_button = wait.until(EC.element_to_be_clickable((By.XPATH, "//a[contains(@class, 'dropdown-item') and contains(text(), 'Logout')]")))
                    logout_button.click()
                    print(f"🔄 Logged out for: {username}")
                    time.sleep(3)

                except Exception as logout_error:
                    print(f"⚠️ Logout failed for {username}: {str(logout_error)}")

            except:
                print(f"❌ Login failed for: {username}")
                output_data.append(row + ["Fail"])

        except Exception as e:
            print(f"⚠️ Error logging in with {username}: {str(e)}")
            output_data.append(row + ["Error"])

        # Save results after each iteration
        with open(output_file, "w", newline="") as file:
            writer = csv.writer(file)
            writer.writerows(output_data)

print(f"✅ Results saved to {output_file}")

# Close browser
driver.quit()
