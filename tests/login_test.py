

class TestLoginPage:

    def test_login(self, main_page,login_page):
        profile = main_page.element_is_attached(
            main_page.PROFILE_DROPDOWN, 30)
        profile_name = ('Britanney Byers' in profile.text)

        assert profile_name == True
