import allure
from pages.base_page import BasePage
from locators.main_page_locators import MainPageLocators as Mpl
from urls import PageURL as Url


class MainPage(BasePage):

    @allure.step("Open main page")
    def open_main_page(self):
        self.get_url(Url.MAIN_PAGE)
        self.check_presence_of_element(Mpl.MAKE_BURGER_HEADER)

    @allure.step("Click on an ingredient")
    def click_on_ingredient(self, ingredient_locator):
        self.click_on_element(ingredient_locator)
        self.check_presence_of_element(Mpl.INGREDIENT_DETAILS)

    @allure.step("Close an ingredient popup")
    def close_ingredient_pop_up_window(self):
        self.click_on_element(Mpl.CLOSE_INGREDIENT_POPUP)
        self.wait_for_closing(Mpl.INGREDIENT_DETAILS)

    @allure.step("Close an order popup")
    def close_order_pop_up_window(self):
        self.click_on_element(Mpl.CLOSE_POPUP_ORDER)
        self.wait_for_closing(Mpl.ORDER_POP_UP)

    @allure.step("Add an ingredient to the order")
    def add_ingredient_to_the_order(self, ingredient_locator):
        self.drag_and_drop_elements(ingredient_locator, Mpl.BOTTOM_BUN)

    @allure.step("Click on make order button")
    def click_make_order(self):
        self.click_on_element(Mpl.MAKE_ORDER_BUTTON)
        self.check_presence_of_element(Mpl.ORDER_ID)

    @allure.step("Making order")
    def make_order(self, ingredients):
        self.open_main_page()
        for ingredient in ingredients:
            self.scroll_to_element(ingredient)
            self.add_ingredient_to_the_order(ingredient)
        self.click_make_order()
        self.wait_for_text_not_to_be_presented(Mpl.ORDER_ID, "9999")
        order_id = self.check_presence_of_element(Mpl.ORDER_ID).text
        self.close_order_pop_up_window()
        return order_id

    @allure.step("Check presence of 'Ingredient details'")
    def check_presence_of_ingredient_details(self):
        element = self.check_presence_of_element(Mpl.INGREDIENT_DETAILS)
        return element

    @allure.step("Check presence of 'Make burger' header")
    def check_presence_of_make_burger_header(self):
        element = self.check_presence_of_element(Mpl.MAKE_BURGER_HEADER)
        return element

    @allure.step("Check presence of 'Make order' button")
    def check_presence_of_make_order_button(self):
        element = self.check_presence_of_element(Mpl.MAKE_ORDER_BUTTON)
        return element




