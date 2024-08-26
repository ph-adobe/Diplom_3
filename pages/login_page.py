import allure
from pages.base_page import BasePage
from locators.login_page_locators import LoginPageLocators as Lpl
from urls import PageURL as Url


class LoginPage(BasePage):
    @allure.step("Get login page")
    def get_login_page(self):
        self.get_url(Url.LOGIN_PAGE)
        self.check_presence_of_element(Lpl.ENTRY_HEADER)

    @allure.step("UI: login")
    def login(self, login_data):
        self.get_login_page()
        self.input_data(Lpl.INPUT_EMAIL, login_data["email"])
        self.input_data(Lpl.INPUT_PASSWORD, login_data["password"])
        self.click_on_element(Lpl.ENTRY_BUTTON)

    @allure.step("Click recover password")
    def click_recover_password(self):
        self.get_login_page()
        self.click_on_element(Lpl.RECOVERY_PASSWORD_LINK)

    @allure.step("Check presence of the login entry header")
    def check_presence_of_login_entry_header(self):
        element = self.check_presence_of_element(Lpl.ENTRY_HEADER)
        return element

