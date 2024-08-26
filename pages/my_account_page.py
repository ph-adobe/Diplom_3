import allure
from pages.base_page import BasePage
from locators.my_account_page_locators import MyAccountPageLocators as Mapl


class MyAccount(BasePage):

    @allure.step("UI: logout")
    def log_out(self):
        self.go_to_my_account()
        self.click_on_element(Mapl.LOGOUT_BUTTON)

    @allure.step("Open order history")
    def open_order_history(self):
        self.go_to_my_account()
        self.click_on_element(Mapl.ORDER_HISTORY)

    @allure.step("Return orders ids from order history")
    def return_list_orders_ids(self):
        self.open_order_history()
        self.check_presence_of_element(Mapl.MY_ORDERS)
        order_ids = []
        orders = self.find_elements(Mapl.MY_ORDERS)
        for order in orders:
            order_id = order.get_attribute("href").split("/")[-1]
            order_ids.append(order_id)
        return order_ids

    @allure.step("Check presence of the profile header")
    def check_presence_of_profile_header(self):
        element = self.check_presence_of_element(Mapl.PROFILE_HEADER)
        return element



