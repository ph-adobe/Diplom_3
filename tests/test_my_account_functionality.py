import allure
from pages.my_account_page import MyAccount
from pages.login_page import LoginPage


class TestMyAccount:
    @allure.title("Test go to my account")
    def test_go_to_my_account(self,  driver, login_user):
        my_account = MyAccount(driver)
        my_account.go_to_my_account()
        element = my_account.check_presence_of_profile_header()

        assert element.is_displayed()

    @allure.title("Test open orders history")
    def test_go_to_order_history(self,  driver, login_user):
        my_account = MyAccount(driver)
        my_account.go_to_my_account()
        my_account.open_order_history()

        assert "order-history" in my_account.current_url

    @allure.title("Test logout")
    def test_logout(self,  driver, login_user):
        my_account = MyAccount(driver)
        login_page = LoginPage(driver)
        my_account.log_out()
        element = login_page.check_presence_of_login_entry_header()

        assert element.is_displayed()

