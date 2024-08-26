import allure
from helpers import GenerateOrderData as Od
from pages.main_page import MainPage
from pages.order_feed import OrderFeedPage


class TestMainFunctionalities:

    @allure.title("Test opening constructor")
    def test_open_constructor(self, driver):
        main_page = MainPage(driver)
        feed_page = OrderFeedPage(driver)
        feed_page.get_order_feed_page()
        main_page.go_to_constructor()
        element = main_page.check_presence_of_make_burger_header()

        assert element

    @allure.title("Test opening order feed")
    def test_open_order_feed(self, driver):
        main_page = MainPage(driver)
        order_feed_page = OrderFeedPage(driver)
        main_page.check_presence_of_make_burger_header()
        order_feed_page.get_order_feed_page()

        assert "/feed" in order_feed_page.current_url

    @allure.title("Test opening ingredient card")
    def test_open_ingredient_card(self, driver):
        main_page = MainPage(driver)
        main_page.click_on_element(Od.return_random_ingredient())
        element = main_page.check_presence_of_ingredient_details()

        assert element.is_displayed()

    @allure.title("Test closing ingredient card")
    def test_ingredient_card_popup_close(self, driver):
        main_page = MainPage(driver)
        main_page.click_on_element(Od.return_random_ingredient())
        element = main_page.check_presence_of_ingredient_details()
        main_page.close_ingredient_pop_up_window()
        result = not element.is_displayed()

        assert result

    @allure.title("Test increasing ingredient count")
    def test_increasing_count(self, driver):
        main_page = MainPage(driver)
        ingredient, counter = Od.return_random_ingredient_with_counter()
        count_before_adding_ingredient = int(main_page.check_presence_of_element(counter).text)
        main_page.add_ingredient_to_the_order(ingredient)
        count_after_adding_ingredient = int(main_page.check_presence_of_element(counter).text)
        delta = count_after_adding_ingredient - count_before_adding_ingredient

        assert delta > 0

    @allure.title("Test that an authenticated user can click on 'Make order' button")
    def test_make_order_by_authenticated_user(self, driver, login_user):
        main_page = MainPage(driver)
        main_page.check_presence_of_make_burger_header()
        element = main_page.check_presence_of_make_order_button()

        assert "Оформить заказ" in element.text




