from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager

# Setup Chrome options to disable notifications pop-ups
chrome_options = Options()
chrome_options.add_experimental_option("prefs", {
    "profile.default_content_setting_values.notifications": 2
})

# Initialize WebDriver
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=chrome_options)
driver.maximize_window()

try:
    # **Step 1: Open Website & Login**
    driver.get("https://allenplus.allen.ac.in/")  

    wait = WebDriverWait(driver, 15)

    # Locate username & password fields and enter credentials
    username = wait.until(EC.presence_of_element_located((By.XPATH, "//input[@name='user']")))
    password = driver.find_element(By.XPATH, "//input[@name='pass']")

    username.send_keys("dumst20")  # Replace with actual username
    password.send_keys("dstd#123")  # Replace with actual password

    # Handle Captcha manually
    captcha = driver.find_element(By.XPATH, "//input[@id='reg-code']")
    captcha.click()
    time.sleep(10)  # Time to enter captcha manually

    login_button = driver.find_element(By.XPATH, "//button[@type='submit']")
    login_button.click()
    time.sleep(5)

    print("✅ Login successful!")

    # **Step 2: Navigate to Schedule Page**
    schedule_button = wait.until(EC.element_to_be_clickable((By.XPATH, "//span[normalize-space()='Schedule']")))
    schedule_button.click()
    time.sleep(3)

    print("✅ Navigated to Schedule page")

    # **Step 3: Capture Notification Count Before Clicking**
    try:
        bell_icon = wait.until(EC.element_to_be_clickable((By.XPATH, "//img[@class='bell-icons']")))
        notification_count_element = bell_icon.find_element(By.XPATH, ".//span[@class='badge']")
        notification_count_before = int(notification_count_element.text.strip()) if notification_count_element.text.strip().isdigit() else 0
        print(f"🔔 Notification count before clicking: {notification_count_before}")
    except:
        print("🔔 No notifications found before clicking.")
        notification_count_before = 0

    # **Step 4: Click the Bell Icon to Open Notifications**
    bell_icon.click()
    print("✅ Clicked on notification bell")
    time.sleep(3)

    # **Step 5: Read Notifications**
    try:
        notification_list = wait.until(EC.presence_of_element_located((By.XPATH, "//ul[@class='notii-wrap table-responsive scroll-tab']/li")))
        notifications = driver.find_elements(By.XPATH, "//ul[@id='notification-list']/li")
        
        print(f"📩 Total notifications found: {len(notifications)}")
        for index, notification in enumerate(notifications, start=1):
            print(f"🔹 Notification {index}: {notification.text.strip()}")

    except:
        print("📭 No new notifications found.")

    # **Step 6: Capture Notification Count After Clicking**
    try:
        notification_count_element = wait.until(EC.presence_of_element_located((By.XPATH, "//span[@id='notification-count']")))
        notification_count_after = int(notification_count_element.text.strip()) if notification_count_element.text.strip().isdigit() else 0
        print(f"🔔 Notification count after clicking: {notification_count_after}")
    except:
        print("🔔 No notifications found after clicking.")
        notification_count_after = 0

    # **Step 7: Check for 'Mark all as read' and 'View all notifications' options**
    try:
        mark_all_read = driver.find_element(By.XPATH, "//button[text()='Mark all as read']")
        view_all_notifications = driver.find_element(By.XPATH, "//a[text()='View all notifications']")

        if mark_all_read:
            print("✅ 'Mark all as read' button is present.")

        if view_all_notifications:
            print("✅ 'View all notifications' link is present.")

    except:
        print("❌ 'Mark all as read' or 'View all notifications' not found.")

    # **Step 8: Compare Notification Counts**
    if notification_count_before > notification_count_after:
        print(f"✅ Notifications read successfully. {notification_count_before - notification_count_after} notifications marked as read.")
    else:
        print("ℹ️ No new notifications were marked as read.")

except Exception as e:
    print("❌ Error:", str(e))

finally:
    driver.quit()
