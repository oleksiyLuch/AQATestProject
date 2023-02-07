from pytest_html_reporter import attach
import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from lib.credentials import Credentials as USER

from pages.login_page import LoginPage
from pages.main_page import MainPage


@pytest.fixture()
def driver():
    driver_service = Service(ChromeDriverManager().install())
    options = webdriver.ChromeOptions()
    # options.add_argument('headless')
    options.add_argument('--disable-infobars')
    options.add_argument('--disable-dev-shm-usage')
    options.add_argument('--no-sandbox')
    options.add_experimental_option("excludeSwitches", ["enable-automation"])
    options.add_experimental_option('useAutomationExtension', False)
    options.add_argument('--remote-debugging-port=9222')
    driver = webdriver.Chrome(options=options, service=driver_service)
    driver.set_window_size("1920", "1080")
    driver.get('https://www.booking.com/')
    yield driver

    driver.quit()


def pytest_addoption(parser):
    parser.addoption('--repeat', action='store',
                     help='Number of times to repeat each test')


def pytest_generate_tests(metafunc):
    if metafunc.config.option.repeat is not None:
        count = int(metafunc.config.option.repeat)

        # We're going to duplicate these tests by parametrizing them,
        # which requires that each test has a fixture to accept the parameter.
        # We can add a new fixture like so:
        metafunc.fixturenames.append('tmp_ct')

        # Now we parametrize. This is what happens when we do e.g.,
        # @pytest.mark.parametrize('tmp_ct', range(count))
        # def test_foo(): pass
        metafunc.parametrize('tmp_ct', range(count))


def pytest_runtest_makereport(item, call) -> None:
    if call.when == "call":
        if call.excinfo is not None and "driver" in item.funcargs:
            page = item.funcargs["driver"]
            attach(data=page.get_screenshot_as_png())


@pytest.fixture()
def login_page(driver):
    login_page = LoginPage(driver)
    login_page.user_login()
    yield login_page

@pytest.fixture()
def main_page(driver):
    main_page = MainPage(driver)
    yield main_page
