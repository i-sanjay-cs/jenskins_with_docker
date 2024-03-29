from selenium import webdriver
from selenium.webdriver.common.by import By

# Set Chrome options and set headless mode
options = webdriver.ChromeOptions()
options.add_argument("--headless")
options.binary_location = r"C:\\Program Files\\Google\\Chrome\\Application\\chrome.exe"  # Specify the Chrome executable path here

# Create a new instance of the Chrome driver with options
driver = webdriver.Chrome(options=options)

# Navigate to the Saucedemo login page
driver.get("https://www.saucedemo.com/")
# Rest of your script remains the same...


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
