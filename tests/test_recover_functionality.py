import allure
from helpers import GenerateUserData as Ud
from pages.forgot_pass_page import ForgotPass
from pages.login_page import LoginPage
from pages.reset_pass_page import ResetPassPage


class TestRecoverPassword:

    @allure.title("Test transfer to the password recovery page")
    def test_go_to_password_recovery_page(self, driver):
        login_page = LoginPage(driver)
        forgot_pass_page = ForgotPass(driver)
        login_page.click_recover_password()
        element = forgot_pass_page.check_presence_pass_recovery_header()

        assert element.is_displayed()

    @allure.title("Test email input for password recovery page")
    def test_input_email_for_recovery(self, driver):
        forgot_pass_page = ForgotPass(driver)
        reset_pass_page = ResetPassPage(driver)
        forgot_pass_page.get_forget_pass_url()
        forgot_pass_page.input_email(Ud.return_email())
        element = reset_pass_page.check_presence_of_pass_field()

        assert element.is_displayed()

    @allure.title("Test that click on the eye-button makes the password field active.")
    def test_eye_button(self, driver):
        forgot_pass_page = ForgotPass(driver)
        reset_pass_page = ResetPassPage(driver)
        forgot_pass_page.get_forget_pass_url()
        forgot_pass_page.input_email(Ud.return_email())
        reset_pass_page.input_password(Ud.return_password())
        reset_pass_page.click_on_input_code_from_email()  # клик по другому полю, чтобы сделать поле пароля неактивным
        reset_pass_page.click_on_eye_button()
        element = reset_pass_page.check_presence_of_pass_field()
        data_type = element.get_attribute("type")

        assert element.is_enabled()  # проверяем, что поле становится активным
        assert data_type == "text"   # проверяем, что при клике на кнопку глаза меняется тип данных в поле

