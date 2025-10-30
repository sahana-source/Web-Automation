from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from pages.login import LoginPage
from pages.shop import ShopPage
from pages.checkout_confirmation import Checkout_Confirmation


def test_shop_checkout_success(browser):
    """
    End-to-end flow:
      1) Login
      2) Add 'Blackberry' to cart
      3) Go to cart and checkout
      4) Enter address and submit
      5) Validate success message
    """
    # 1) Login
    login = LoginPage(browser)
    # If your LoginPage has open(), use it; otherwise navigate here:
    try:
        login.open()
    except AttributeError:
        browser.get("https://rahulshettyacademy.com/loginpagePractise/")
    login.login("rahulshettyacademy", "learning")

    # Wait for shop page (product cards visible)
    WebDriverWait(browser, 10).until(
        EC.visibility_of_element_located((By.CSS_SELECTOR, ".card"))
    )

    # 2) Add product to cart
    shop = ShopPage(browser)
    shop.add_product_to_cart("Blackberry")

    # 3) Go to cart
    cc: Checkout_Confirmation = shop.goToCart()

    # 4) Checkout and submit address
    cc.checkout()
    cc.enter_delivery_address("India")

    # 5) Validate success
    cc.validate_order()
