from pages.login_page import LoginPage
from lib.credentials import Credentials as USER


class TestLoginPage:

    def test_login(self, driver):
        login_page = LoginPage(driver, 'https://www.booking.com/')
        login_page.open()
        login_page.click(login_page.SIGNIN_BUTTON)
        login_page.fill_field(login_page.EMAIL_FIELD, USER.LOGIN)
        login_page.click(login_page.CONTINUE_WITH_EMAIL_BUTTON)
        login_page.fill_field(login_page.PASSWORD_FIELD, USER.PASSWORD)
        login_page.click(login_page.SUBMIT_PASSWORD_BUTTON)
        profile = login_page.element_is_visible(login_page.PROFILE_DROPDOWN,30)
        profile_name = ('Britanney Byers' in profile.text)

        assert profile_name == False

