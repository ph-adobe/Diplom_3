import allure
from pages.base_page import BasePage
from locators.order_feed_locatorrs import OrderFeedLocators as Ofl
import random


class OrderFeedPage(BasePage):
    @allure.step("Get Orders feed page")
    def get_order_feed_page(self):
        self.open_order_feed()
        self.check_presence_of_element(Ofl.ORDER_FEED_HEADER)

    @allure.step("Return all orders from orders feed")
    def return_all_orders(self):
        self.open_order_feed()
        self.check_presence_of_element(Ofl.ALL_ORDERS)
        elements = self.find_elements(Ofl.ALL_ORDERS)
        return elements

    @allure.step("Return all orders ids from orders feed")
    def return_all_orders_ids(self):
        order_ids = []
        orders = self.return_all_orders()
        for order in orders:
            order_id = order.get_attribute("href").split("/")[-1]
            order_ids.append(order_id)
        return order_ids

    @allure.step("Click on order")
    def click_on_order(self):
        elements = self.return_all_orders()
        order = random.choice(elements)
        self.scroll_to_element_use_element_itself(order)
        order.click()

    @allure.step("Get orders from 'All orders for all time'")
    def get_number_of_orders_for_all_time(self):
        self.get_order_feed_page()
        number = int(self.check_presence_of_element(Ofl.ORDERS_NUMBER_ALL_TIME).text)
        return number

    @allure.step("Get orders from 'All orders for today'")
    def get_number_of_orders_for_today(self):
        self.get_order_feed_page()
        number = int(self.check_presence_of_element(Ofl.ORDERS_NUMBER_ALL_TIME).text)
        return number

    @allure.step("Get value from 'In progress' field")
    def get_value_from_in_progress_field(self):
        element = self.check_presence_of_element(Ofl.ORDERS_IN_PROGRESS)
        return element.text

    @allure.step("Check presence of order popup")
    def check_presence_of_order_popup(self):
        element = self.check_presence_of_element(Ofl.ORDER_POP_UP)
        return element








