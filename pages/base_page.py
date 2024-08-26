import allure
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.action_chains import ActionChains
from locators.base_page_locators import BasePageLocators as Bpl


class BasePage:
    timeout = 10

    def __init__(self, driver):
        self.driver = driver

    @property
    def current_url(self):
        return self.driver.current_url

    @allure.step("Open page")
    def get_url(self, url):
        self.driver.get(url)

    @allure.step("Wait until text is not presented in the element")
    def wait_for_text_not_to_be_presented(self, element_locator, text, time=timeout):
        WebDriverWait(
                self.driver, timeout=time).until_not(
                expected_conditions.text_to_be_present_in_element(element_locator, text)
            )

    @allure.step("Wait until windows is closed")
    def wait_for_closing(self, locator, time=timeout):
        WebDriverWait(self.driver, time).until(expected_conditions.invisibility_of_element_located(locator))

    @allure.step("Check presence of the element")
    def check_presence_of_element(self, element_locator):
        element = WebDriverWait(self.driver, self.timeout).until(
            expected_conditions.presence_of_element_located(element_locator),
            message=f"Not found: {element_locator}",
        )
        return element

    @allure.step("Find elements")
    def find_elements(self, locator):
        elements = self.driver.find_elements(*locator)
        return elements

    @allure.step("Scroll to the element (using element locator)")
    def scroll_to_element(self, element_locator):
        element = self.check_presence_of_element(element_locator)
        self.driver.execute_script("arguments[0].scrollIntoView();", element)
        WebDriverWait(self.driver, self.timeout).until(expected_conditions.element_to_be_clickable(element_locator))
        return element

    @allure.step("Scroll to the element (using element itself)")
    def scroll_to_element_use_element_itself(self, element):
        self.driver.execute_script("arguments[0].scrollIntoView();", element)
        WebDriverWait(self.driver, self.timeout).until(expected_conditions.element_to_be_clickable(element))

    @allure.step("Click on the element")
    def click_on_element(self, element_locator):
        self.scroll_to_element(element_locator)
        self.check_presence_of_element(element_locator).click()

    @allure.step("Input data into the field")
    def input_data(self, element_locator, *args):
        self.check_presence_of_element(element_locator).click()
        self.check_presence_of_element(element_locator).send_keys(*args)

    @allure.step("Drag and drop the element to the given destination")
    def drag_and_drop_elements(self, element_locator_source, element_locator_destination):
        action = ActionChains(self.driver)
        source = self.check_presence_of_element(element_locator_source)
        destination = self.check_presence_of_element(element_locator_destination)
        action.drag_and_drop(source, destination).perform()

    @allure.step("Go to My account")
    def go_to_my_account(self):
        self.click_on_element(Bpl.MY_ACCOUNT_BUTTON)

    @allure.step("Go to Constructor")
    def go_to_constructor(self):
        self.click_on_element(Bpl.CONSTRUCTOR_BUTTON)

    @allure.step("Go to Orders feed")
    def open_order_feed(self):
        self.click_on_element(Bpl.ORDER_FEED_BUTTON)




