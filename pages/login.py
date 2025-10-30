from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from utils.browserutils import BrowserUtils

class LoginPage(BrowserUtils):
    URL = "https://rahulshettyacademy.com/loginpagePractise/"

    def __init__(self, driver, timeout: int = 10):
        super().__init__(driver)
        self.wait = WebDriverWait(driver, timeout)
        self.username_input = (By.ID, "username")
        self.password_input = (By.NAME, "password")  # renamed for clarity
        self.sign_button = (By.ID, "signInBtn")
        self.error_banner = (By.CSS_SELECTOR, "div.alert-danger")

    def open(self):
        self.driver.get(self.URL)
        self.wait.until(EC.element_to_be_clickable(self.username_input))

    def login(self, username, password):
        self.wait.until(EC.visibility_of_element_located(self.username_input)).send_keys(username)
        self.wait.until(EC.visibility_of_element_located(self.password_input)).send_keys(password)
        self.wait.until(EC.element_to_be_clickable(self.sign_button)).click()

    def get_error_text(self):
        return self.wait.until(EC.visibility_of_element_located(self.error_banner)).text
