import allure
from pages.base_page import BasePage
from locators.reset_pass_page_locators import ResetPassLocators as Rpl


class ResetPassPage(BasePage):
    @allure.step("Input password into reset password field")
    def input_password(self, password):
        self.check_presence_of_element(Rpl.PASSWORD_FIELD)
        self.input_data(Rpl.PASSWORD_FIELD, password)

    @allure.step("Click on eye button")
    def click_on_eye_button(self):
        self.click_on_element(Rpl.EYE_BUTTON)

    @allure.step("Change focus to another field")
    def click_on_input_code_from_email(self):
        self.click_on_element(Rpl.INPUT_CODE_FROM_EMAIL)

    @allure.step("Check presence of password field")
    def check_presence_of_pass_field(self):
        self.click_on_element(Rpl.INPUT_CODE_FROM_EMAIL)
        element = self.check_presence_of_element(Rpl.PASSWORD_FIELD)
        return element

