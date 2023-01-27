from pages.base_page import BasePage
from selenium.webdriver.common.by import By


class LoginPage(BasePage):
    # ORIGIN_FIELD = (By.CSS_SELECTOR, '#search-departure-station')
    EMAIL_FIELD = (By.CSS_SELECTOR, '[name="username"]')
    PASSWORD_FIELD = (By.CSS_SELECTOR, '[name="password"]')
    CONTINUE_WITH_EMAIL_BUTTON = (By.XPATH, '//button/span[text()="Continue with email"]')
    SIGNIN_BUTTON = (By.LINK_TEXT, 'Sign in')
    SUBMIT_PASSWORD_BUTTON = (By.XPATH, '//*[text()="Sign in"]')

    def __init__(self, driver, url):
        super().__init__(driver, url)
        self.driver = driver
        self.url = url

