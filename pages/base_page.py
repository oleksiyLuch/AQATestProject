from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait as Wait
from selenium.webdriver.support import expected_conditions as EC


class BasePage:
    PROFILE_DROPDOWN = (By.CSS_SELECTOR, '[data-bui-component="Dropdown"]')

    def __init__(self, driver, url):
        self.driver = driver
        self.url = url

    def open(self):
        self.driver.get(self.url)

    def accept_cookies(self):
        accept_button = (By.CSS_SELECTOR, '[data-test="CookiesPopup-Accept"]')
        self.element_is_visible(accept_button).click()

    def element_is_visible(self, locator, timeout=15):
        return Wait(self.driver, timeout).until(EC.visibility_of_element_located(locator))

    def elements_are_visible(self, locator, timeout=5):
        return Wait(self.driver, timeout).until(EC.visibility_of_all_elements_located(locator))

    def element_is_attached(self, locator, timeout=15):
        return Wait(self.driver, timeout).until(EC.presence_of_element_located(locator))

    def click(self, locator, timeout=5):
        return Wait(self.driver, timeout).until(EC.element_to_be_clickable(locator)).click()

    def fill_field(self, locator, text):
        return self.element_is_visible(locator).send_keys(text)

    def check(self):
        pass

    def filter(self):
        pass
