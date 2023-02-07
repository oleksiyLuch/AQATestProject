from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait as Wait
from selenium.webdriver.support import expected_conditions as EC

from pages.base_page import BasePage


class MainPage(BasePage):
    PROFILE_DROPDOWN = (By.XPATH, '//*[text()="Britanney Byers"]')

    def __init__(self, driver, url='https://www.booking.com/'):
        super().__init__(driver, url)
        self.page = driver
        self.url = url
