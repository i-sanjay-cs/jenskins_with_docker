from selenium import webdriver
from selenium.webdriver.common.by import By

# Set ChromeDriver path
chrome_driver_path = r"C:\\Users\\sanja\\Downloads\\chromedriver-win64 (1)\\chromedriver.exe"

# Create a new instance of the Chrome driver
driver = webdriver.Chrome(executable_path=chrome_driver_path)

# Navigate to the Saucedemo login page
driver.get("https://www.saucedemo.com/")

# Enter username and password
username_input = driver.find_element(By.ID, "user-name")
password_input = driver.find_element(By.ID, "password")
username_input.send_keys("standard_user")
password_input.send_keys("secret_sauce")

# Click the login button
login_button = driver.find_element(By.ID, "login-button")
login_button.click()

# Verify if login is successful
if "inventory.html" in driver.current_url:
    print("Login Successful!")
else:
    print("Login Failed!")

# Close the browser
driver.quit()
