import allure
from helpers import GenerateOrderData as Od
from pages.main_page import MainPage
from pages.my_account_page import MyAccount
from pages.order_feed import OrderFeedPage


class TestOrderFeedPage:

    @allure.title("Test opening order popup window")
    def test_appearing_order_popup(self, driver):
        order_feed = OrderFeedPage(driver)
        order_feed.click_on_order()
        element = order_feed.check_presence_of_order_popup()

        assert element.is_displayed()

    @allure.title("Test appearance of orders from account in orders feed")
    def test_orders_from_account_in_orders_feed(self, driver, login_user_with_orders):
        my_account = MyAccount(driver)
        my_account_orders = my_account.return_list_orders_ids()
        order_feed = OrderFeedPage(driver)
        all_orders = order_feed.return_all_orders_ids()

        result = []
        for order in my_account_orders:
            result.append(order in all_orders)

        assert all(result)

    @allure.title("Test increasing number of orders for all time after the order has been made")
    def test_increasing_orders_number_for_all_time(self, driver, login_user):
        main_page = MainPage(driver)
        order_feed = OrderFeedPage(driver)
        all_orders_number_before = order_feed.get_number_of_orders_for_all_time()
        main_page.make_order(Od.return_ingredients_to_order())
        order_feed.open_order_feed()
        all_orders_number_after = order_feed.get_number_of_orders_for_all_time()

        delta = all_orders_number_after - all_orders_number_before

        assert delta >= 1

    @allure.title("Test increasing number of orders for today after the order has been made")
    def test_increasing_orders_number_for_today(self, driver, login_user):
        main_page = MainPage(driver)
        order_feed = OrderFeedPage(driver)
        today_orders_number_before = order_feed.get_number_of_orders_for_today()
        main_page.make_order(Od.return_ingredients_to_order())
        order_feed.open_order_feed()
        today_orders_number_after = order_feed.get_number_of_orders_for_today()

        delta = today_orders_number_after - today_orders_number_before

        assert delta >= 1

    @allure.title("Test appearing the order id in 'In progress' field")
    def test_order_id_in_progress_field(self, driver, login_user):
        main_page = MainPage(driver)
        order_feed = OrderFeedPage(driver)
        order_id = main_page.make_order(Od.return_ingredients_to_order())
        order_feed.get_order_feed_page()
        in_progress_field = order_feed.get_value_from_in_progress_field()

        assert order_id in in_progress_field

