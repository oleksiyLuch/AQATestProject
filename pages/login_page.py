from pages.base_page import BasePage
from selenium.webdriver.common.by import By
from lib.credentials import Credentials as USER


class LoginPage(BasePage):
    # ORIGIN_FIELD = (By.CSS_SELECTOR, '#search-departure-station')
    EMAIL_FIELD = (By.CSS_SELECTOR, '[name="username"]')
    PASSWORD_FIELD = (By.CSS_SELECTOR, '[name="password"]')
    CONTINUE_WITH_EMAIL_BUTTON = (
        By.XPATH, '//button/span[text()="Continue with email"]')
    SIGNIN_BUTTON = (By.LINK_TEXT, 'Sign in')
    SUBMIT_PASSWORD_BUTTON = (By.XPATH, '//*[text()="Sign in"]')

    def __init__(self, driver, url='https://www.booking.com/'):
        super().__init__(driver, url)
        self.page = driver
        self.url = url

    def user_login(self):
        self.click(self.SIGNIN_BUTTON)
        self.fill_field(self.EMAIL_FIELD, USER.LOGIN)
        self.click(self.CONTINUE_WITH_EMAIL_BUTTON)
        self.fill_field(self.PASSWORD_FIELD, USER.PASSWORD)
        self.click(self.SUBMIT_PASSWORD_BUTTON)
