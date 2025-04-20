from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager
import traceback
import time

# Setup Chrome options
options = Options()
options.add_argument("--headless=new")  # Use headless mode
options.add_argument("--no-sandbox")
options.add_argument("--disable-dev-shm-usage")
options.add_argument("--disable-gpu")
options.add_argument("--remote-debugging-port=9223")
options.add_argument("user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36")

# Specify the Chromium binary location explicitly (if needed)
options.binary_location = "/usr/bin/chromium"  # Adjust this path if necessary

# Start Chrome using WebDriverManager
print("🚀 Launching browser...")
service = Service("/usr/local/bin/chromedriver")  # Path to the installed ChromeDriver
driver = webdriver.Chrome(service=service, options=options)

try:
    # Navigate to Wikipedia
    driver.get("https://www.wikipedia.org")
    print("✅ Page title:", driver.title)

    # Wait for the search box to appear and interact with it
    search_box = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.ID, "searchInput"))  # Wikipedia's search input field
    )
    print("🔍 Found search box")

    # Enter search query and submit
    search_box.send_keys("Selenium Python")
    search_box.send_keys(Keys.RETURN)
    print("📤 Sent search query")

    # Wait for the content area to appear
    content_area = WebDriverWait(driver, 20).until(
        EC.presence_of_element_located((By.ID, "mw-content-text"))  # Wikipedia's main content area
    )
    print("📦 Content area loaded")

    # Add a small delay to ensure content is fully rendered
    time.sleep(2)

    # Fetch and print the first 5 paragraphs or headings
    paragraphs = content_area.find_elements(By.XPATH, ".//p | .//h2")  # Get paragraphs and headings

    if len(paragraphs) == 0:
        print("❌ No content found!")
        # Debug: Print the container's HTML to inspect the structure
        print("🔍 Debugging - Content HTML:", content_area.get_attribute("outerHTML"))
    else:
        print("\n📄 First 5 content items:")
        for i, item in enumerate(paragraphs[:5], 1):
            print(f"{i}. {item.text.strip()}")

except Exception as e:
    print("❌ Error during automation:")
    traceback.print_exc()

finally:
    # Close the browser
    driver.quit()
    print("🧹 Closed browser")