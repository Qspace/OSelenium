from selenium import webdriver
from selenium.webdriver.chrome.options import Options

# Set up Chrome options for headless mode
chrome_options = Options()
chrome_options.add_argument("--headless")  # Run without GUI
chrome_options.add_argument("--no-sandbox")  # Required for Codespaces
chrome_options.add_argument("--disable-dev-shm-usage")  # Avoid resource issues

# Initialize the WebDriver
driver = webdriver.Chrome(options=chrome_options)

# Test by visiting a website
driver.get("https://www.example.com")
print(driver.title)  # Should print "Example Domain"

# Clean up
driver.quit()