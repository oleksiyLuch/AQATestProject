import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

@pytest.fixture()
def driver():
    driver_service = Service(ChromeDriverManager().install())
    options = webdriver.ChromeOptions()
    # options.add_argument('headless')
    options.add_argument('--disable-infobars')
    options.add_argument('--disable-dev-shm-usage')
    options.add_argument('--no-sandbox')
    options.add_argument('--remote-debugging-port=9222')
    driver = webdriver.Chrome(options=options,service=driver_service)
    driver.maximize_window()
    yield driver
    driver.quit()
