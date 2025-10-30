import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
from pages.login import LoginPage

@pytest.fixture(scope="session")
def browser():
    """Launch Chrome browser for the entire test session."""
    opts = Options()
    opts.add_argument("--start-maximized")
    opts.add_argument("--disable-notifications")
    opts.add_argument("--disable-popup-blocking")
    opts.add_argument("--incognito")
    # Uncomment if running in CI/CD or Docker
    # opts.add_argument("--headless=new")
    # opts.add_argument("--no-sandbox")
    # opts.add_argument("--disable-dev-shm-usage")

    service = Service(ChromeDriverManager().install())
    driver = webdriver.Chrome(service=service, options=opts)

    # Implicit wait to handle dynamic elements
    driver.implicitly_wait(10)
    yield driver   # Return the driver to the test
    driver.quit()  # Teardown after all tests


@pytest.fixture(scope="function")
def setup_logged_in(browser):
    """
    Login before each test and return the logged-in ShopPage.
    """
    login_page = LoginPage(browser)
    login_page.open()
    shop_page = login_page.login("rahulshettyacademy", "learning")
    return shop_page