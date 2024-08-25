import allure
from pages.base_page import BasePage
from locators.reset_pass_page_locators import ResetPassLocators as Rpl


class ResetPassPage(BasePage):
    @allure.step("Input password into reset password field")
    def input_password(self, password):
        self.input_data(Rpl.PASSWORD_FIELD, password)

    @allure.step("Click on eye button")
    def click_on_eye_button(self):
        self.click_on_element(Rpl.EYE_BUTTON)

