# import time
# import openpyxl
# from selenium import webdriver
# from selenium.webdriver.common.by import By
# from selenium.webdriver.common.keys import Keys
# from selenium.webdriver.chrome.service import Service
# from webdriver_manager.chrome import ChromeDriverManager
# from openpyxl.styles import PatternFill
# from webdriver_manager.firefox import GeckoDriverManager
# from selenium.webdriver.firefox.service import Service as FirefoxService

# # Load Excel sheet
# file_path = "test_data.xlsx"
# workbook = openpyxl.load_workbook(file_path)
# sheet = workbook.active  # Assuming test data is in the first sheet

# options = webdriver.ChromeOptions()
# options.add_argument("--headless")  # Run without GUI

# # Set up WebDriver
# service = Service(ChromeDriverManager().install())
# # driver = webdriver.Firefox(service=FirefoxService(GeckoDriverManager().install()))
# driver = webdriver.Chrome(service=service)
# driver.maximize_window()

# # Open the login page
# driver.get("https://www.gabrielny.com/customer/account/login/")

# # Loop through test data in Excel
# for row in range(2, sheet.max_row + 1):  # Assuming first row is header
#     username = sheet.cell(row=row, column=1).value
#     password = sheet.cell(row=row, column=2).value

#     if not username or not password:
#         continue  # Skip empty rows

#     try:
#         # Find and fill in login form
#         driver.find_element(By.XPATH, "//input[@id='email']").clear()
#         driver.find_element(By.XPATH, "//input[@id='email']").send_keys(username)

#         driver.find_element(By.XPATH, "//input[@id='pass']").clear()
#         driver.find_element(By.XPATH, "//input[@id='pass']").send_keys(password)

#         # Click login button
#         driver.find_element(By.XPATH, "//button[@id='send2']").click()
#         time.sleep(3)  # Wait for page to load

#         # Check if login was successful
#         if "account" in driver.current_url.lower():  # Successful login redirects to account page
#             sheet.cell(row=row, column=3, value="Pass").fill = PatternFill(start_color="00FF00", fill_type="solid")  # Green
#         else:
#             sheet.cell(row=row, column=3, value="Fail").fill = PatternFill(start_color="FF0000", fill_type="solid")  # Red

#     except Exception as e:
#         sheet.cell(row=row, column=3, value="Fail").fill = PatternFill(start_color="FF0000", fill_type="solid")  # Red

#     finally:
#         driver.get("https://www.gabrielny.com/customer/account/logout/")  # Logout and prepare for next login attempt
#         time.sleep(3)

# # Save results in Excel
# workbook.save(file_path)
# workbook.close()

# # Close the browser
# driver.quit()





from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

options = webdriver.ChromeOptions()
options.add_argument("--headless")  # Run in headless mode
options.add_argument("--disable-gpu")
options.add_argument("--no-sandbox")
options.add_argument("--disable-dev-shm-usage")
options.add_argument("--disable-extensions")
options.add_argument("--user-data-dir=/tmp/chrome-profile")  # Use fresh profile

service = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=service, options=options)

driver.set_page_load_timeout(120)  # Increase timeout

try:
    driver.get("https://www.gabrielny.com/customer/account/login/")
    print("Page loaded successfully!")
except Exception as e:
    print(f"Error: {e}")

driver.quit()


