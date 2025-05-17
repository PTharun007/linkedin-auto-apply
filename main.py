from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException, ElementClickInterceptedException
from dotenv import load_dotenv
import time
import os
from webdriver_manager.chrome import ChromeDriverManager

# --- Load environment variables ---
load_dotenv()
EMAIL = os.getenv("LINKEDIN_EMAIL")
PASSWORD = os.getenv("LINKEDIN_PASSWORD")
PHONE = os.getenv("LINKEDIN_PHONE")

# --- Setup Chrome ---
chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument("--start-maximized")
chrome_options.add_experimental_option("detach", True)
driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()), options=chrome_options)
wait = WebDriverWait(driver, 20)

# --- Step 1: Open LinkedIn Job Page ---
driver.get("https://www.linkedin.com/jobs/search/?currentJobId=4225227036&f_LF=f_AL&geoId=105556991&keywords=python%20developer")
time.sleep(3)

# --- Step 2: Handle Overlay ---
try:
    overlay = driver.find_element(By.CLASS_NAME, "modal__overlay--visible")
    driver.execute_script("arguments[0].style.display = 'none';", overlay)
    print("⚠️ Overlay detected and hidden.")
except NoSuchElementException:
    print("✅ No overlay found.")

# --- Step 3: Click Sign In ---
try:
    sign_in_btn = wait.until(EC.element_to_be_clickable((By.LINK_TEXT, "Sign in")))
    sign_in_btn.click()
    print("➡️ Clicked sign-in.")
except ElementClickInterceptedException:
    print("⚠️ Sign-in button was blocked, trying JavaScript click.")
    driver.execute_script("arguments[0].click();", sign_in_btn)

# --- Step 4: Log in ---
email_field = wait.until(EC.presence_of_element_located((By.ID, "username")))
email_field.send_keys(EMAIL)
password_field = driver.find_element(By.ID, "password")
password_field.send_keys(PASSWORD)
password_field.send_keys(Keys.ENTER)
print("🔐 Logged in successfully.")

# --- Optional: CAPTCHA ---
input("⏸️ If there is a CAPTCHA, solve it and press Enter to continue...")

# --- Step 5: Re-open Job Listing ---
driver.get("https://www.linkedin.com/jobs/search/?currentJobId=4225227036&f_LF=f_AL&geoId=105556991&keywords=python%20developer")
time.sleep(5)

# --- Step 6: Click First Job ---
try:
    first_job = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, ".job-card-container--clickable")))
    first_job.click()
    print("📄 Opened first job listing.")
    time.sleep(3)
except Exception as e:
    print("❌ Failed to open job:", e)
    driver.quit()
    exit()

# --- Step 7: Easy Apply ---
try:
    easy_apply = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, ".jobs-apply-button")))
    easy_apply.click()
    print("🟢 Clicked Easy Apply.")
    time.sleep(2)
except Exception as e:
    print("❌ Easy Apply failed:", e)
    driver.quit()
    exit()

# --- Step 8: Enter Phone Number ---
try:
    phone_input = driver.find_element(By.CSS_SELECTOR, "input[id*=phoneNumber]")
    if phone_input.get_attribute("value") == "":
        phone_input.send_keys(PHONE)
        print("📞 Entered phone number.")
except NoSuchElementException:
    print("⚠️ Phone input not found.")

# --- Step 9: Submit Application ---
try:
    submit_btn = wait.until(EC.element_to_be_clickable((By.XPATH, "//button/span[text()='Submit application']/..")))
    submit_btn.click()
    print("🎉 Successfully submitted application!")
except:
    print("⚠️ Submit button not found. Might be multi-step or require resume.")

# --- Done ---
time.sleep(5)
driver.quit()