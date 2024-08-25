from pages.base_page import BasePage
from locators.forgot_password_locators import ForgotPasswordLocators as Fpl
from urls import PageURL as Url


class ForgotPass(BasePage):
    def get_forget_pass_url(self):
        self.get_url(Url.FORGOT_PASSWORD_PAGE)
        self.check_presence_of_element(Fpl.PASSWORD_RECOVERY_HEADER)

    def input_email(self, email):
        self.get_forget_pass_url()
        self.input_data(Fpl.EMAIL_FIELD, email)
        self.click_on_element(Fpl.RECOVERY_BUTTON)




