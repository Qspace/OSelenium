from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager

# Set up Chrome options with all necessary arguments
options = Options()
options.add_argument("--headless=new")
options.add_argument("--no-sandbox")
options.add_argument("--disable-dev-shm-usage")
options.add_argument("--remote-debugging-port=9222")
options.add_argument("--disable-gpu")

# Specify the Chromium binary location explicitly
options.binary_location = "/usr/bin/chromium"  # Adjust if needed

print("🚀 Launching browser...")
# Specify the correct ChromeDriver version explicitly
service = Service("/usr/local/bin/chromedriver")  # Path to the installed ChromeDriver
driver = webdriver.Chrome(service=service, options=options)

try:
    driver.get("https://www.example.com")
    print("✅ Page title:", driver.title)
finally:
    driver.quit()
    print("🧹 Closed browser")