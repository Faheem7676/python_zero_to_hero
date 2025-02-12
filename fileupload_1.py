from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import os
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

# Initialize WebDriver
service = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=service)

# Open the image upload website
driver.get("https://tus.io/demo.html")
print("Website launched successfully")

# Ensure the file exists before uploading
image_path = os.path.abspath("testingfile.jpg")
if os.path.exists(image_path):
    print("✅ File found:", image_path)
else:
    print("❌ File NOT found:", image_path)
    driver.quit()
    exit()

# Maximize window
driver.maximize_window()
print("Website maximized")

# Get the file input element
file_input = driver.find_element(By.XPATH, "//input[@type='file']")
print("Found the input element")

# Scroll to make the element visible
driver.execute_script("window.scrollBy(0, 500);")
time.sleep(1)

# Highlight the element
driver.execute_script("arguments[0].style.border='3px solid red'", file_input)
print("Highlighted the upload element")

# Upload the image
file_input.send_keys(image_path)
print("Image uploaded successfully")
time.sleep(5)

# ✅ **Dynamically wait for the success message to appear**
try:
    success_message_element = WebDriverWait(driver, 30).until(
        EC.presence_of_element_located((By.XPATH, "//p[text()='The upload is complete!']"))
    )
    print("to findout success message")
    success_message = success_message_element.text
    print("✅ Upload Message:", success_message)
    
    # ✅ **Verify the upload success message**
    if "The upload is complete!" in success_message:
        print("✅ File uploaded successfully! ✅")
    else:
        print("⚠️ Upload message doesn't match expected text!")

except:
    print("❌ No success message found within 10 seconds")

# Close the browser
driver.quit()
