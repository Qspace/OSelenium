import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager
import traceback

# Setup Chrome options
options = Options()
options.add_argument("--headless")
options.add_argument("--no-sandbox")
options.add_argument("--disable-dev-shm-usage")

# Initialize the driver as a fixture
@pytest.fixture(scope="module")  # Use fixture for setup and teardown
def driver():
    print("🚀 Launching browser...")
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)  # Start Chrome
    yield driver  # Provide the fixture value
    driver.quit() # Close the browser after the test
    print("🧹 Closed browser")

def test_google_search(driver): # Pass the driver fixture to the test
    try:
        driver.get("https://www.google.com")
        print("✅ Page title:", driver.title)
        assert "Google" in driver.title # Verify page title

        search_box = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, "//*[@name='q']"))  # Using name attribute for search box
        )
        print("🔍 Found search box")

        search_box.send_keys("selenium python tutorial")
        search_box.send_keys(Keys.RETURN)
        print("📤 Sent search query")

        # Update wait time and XPath for search results
        first_result = WebDriverWait(driver, 120).until(
            EC.presence_of_element_located((By.XPATH, "//h3"))  # Adjust based on current structure
        )

        results = driver.find_elements(By.XPATH, "//h3")  # Update this XPath as per the latest page structure

        assert len(results) > 0, "❌ No results found!" # Assert that results are found

        print("\n📄 Top 5 search results:")
        for i, result in enumerate(results[:5], 1):
            print(f"{i}. {result.text.strip()}")

    except Exception as e:
        print("❌ Error during automation:")
        traceback.print_exc()
        raise  # Re-raise the exception to mark the test as failed
