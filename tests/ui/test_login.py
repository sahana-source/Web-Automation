from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from pages.login import LoginPage


def test_valid_login(browser):
    """
    Test to verify valid login using the LoginPage object.
    """
    login_page = LoginPage(browser)
    login_page.open()  # navigate to login page
    shop_page = login_page.login("rahulshettyacademy", "learning")

    # Wait until a known element on the shop page is visible
    wait = WebDriverWait(browser, 10)
    wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, ".card")))

    # Verify page title or URL
    assert "shop" in browser.current_url.lower(), "Login did not redirect to shop page"
    print("\n✅ Login successful — redirected to shop page.")


def test_invalid_login(browser):
    """
    Test to verify invalid login shows an error message.
    """
    login_page = LoginPage(browser)
    login_page.open()
    login_page.login("wronguser", "wrongpassword")

    # Wait for error message
    wait = WebDriverWait(browser, 10)
    error_message = wait.until(
        EC.visibility_of_element_located((By.CSS_SELECTOR, "div.alert-danger"))
    ).text

    assert "Incorrect" in error_message or "invalid" in error_message.lower(), \
        "Expected error message not displayed."
    print("\n❌ Invalid login test passed — error displayed correctly.")
