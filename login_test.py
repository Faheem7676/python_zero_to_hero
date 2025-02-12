from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

# Setup WebDriver
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
driver.maximize_window()

try:
    # Open the website
    driver.get("URL")  # Replace with the actual login page URL
    
    # Wait for elements to be present
    wait = WebDriverWait(driver, 10)
    
    # Locate username & password fields and enter credentials
    username = wait.until(EC.presence_of_element_located((By.XPATH, "//form/label/input[@name='user']")))  # Change ID as per the website
    password = driver.find_element(By.XPATH, "//form/label/input[@name='pass']")  # Change ID as per the website

    username.send_keys("dumst20")  # Replace with actual username
    password.send_keys("dstd#123")  # Replace with actual password

    
    captcha=driver.find_element(By.XPATH,"//div/label/input[@id='reg-code']")
    captcha.click()
    time.sleep(10)
    
    # Locate and click the login button
    login_button = driver.find_element(By.XPATH, "//button[@type='submit']")  # Change XPath as per the website
    login_button.click()
    
    
    verifyhomeworkbutton=wait.until(EC.presence_of_element_located((By.XPATH, "//nav[@class='no-allen']/ul/li[@id='homeworktour']")))  # Modify verification criteria
    print("verifyhomeworkbutton:",verifyhomeworkbutton.text)
    homeworkelement=verifyhomeworkbutton.text.strip()
    
    if homeworkelement=="Homework":
        verifyhomeworkbutton.click()
        time.sleep(3)
        print("✅ Homework accordian is clicked successfully")
        
    else:
        print("❌ it is not clicked:")
        
    try:
        verifyschedulekbutton = wait.until(EC.presence_of_element_located((By.XPATH, "//span[@class='fadeInRight animated nav-link-name name-hide tax-show'][normalize-space()='Schedule']")))

        # Adding a small delay to allow text to load
        time.sleep(2)

        # Try different methods to extract text
        schedule_text = verifyschedulekbutton.text.strip()
        print("Text from .text:", schedule_text)

        if not schedule_text:
            schedule_text = verifyschedulekbutton.get_attribute("textContent").strip()
            print("Text from get_attribute('textContent'):", schedule_text)

        if not schedule_text:
            schedule_text = verifyschedulekbutton.get_attribute("innerText").strip()
            print("Text from get_attribute('innerText'):", schedule_text)

        # Click using JavaScript if normal click fails
        if schedule_text == "Schedule":
            driver.execute_script("arguments[0].click();", verifyschedulekbutton)
            time.sleep(3)
            print("✅ Schedule accordion is clicked successfully")
        else:
            print("❌ Schedule is not clicked (text mismatch)")

    except Exception as e:
        print("❌ Error with Schedule button:", str(e))

    # Verify login success
    verifystudybutton=wait.until(EC.presence_of_element_located((By.XPATH, "//nav[@class='no-allen']/ul/li[@id='studytour']")))  # Modify verification criteria
    print("verifystudybutton:",verifystudybutton.text)
    studyelement=verifystudybutton.text.strip()
    
    if studyelement=="Study":
        verifystudybutton.click()
        time.sleep(3)
        print("✅ Study accordian is clicked successfully")
    else:
        print("❌ it is not clicked:")
    print("✅ Login successful!")

except Exception as e:
    print("❌ Login failed:", str(e))

finally:
    driver.quit()
