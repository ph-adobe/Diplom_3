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

    def get_url(self, url):
        self.driver.get(url)

    def wait_for_text_not_to_be_presented(self, element_locator, text, time=timeout):
        WebDriverWait(
                self.driver, timeout=time).until_not(
                expected_conditions.text_to_be_present_in_element(element_locator, text)
            )

    def wait_for_closing(self, locator, time=timeout):
        WebDriverWait(self.driver, time).until(expected_conditions.invisibility_of_element_located(locator))

    def check_presence_of_element(self, element_locator):
        element = WebDriverWait(self.driver, self.timeout).until(
            expected_conditions.presence_of_element_located(element_locator),
            message=f"Not found: {element_locator}",
        )
        return element

    def find_elements(self, locator):
        elements = self.driver.find_elements(*locator)
        return elements

    def scroll_to_element(self, element_locator):
        element = self.check_presence_of_element(element_locator)
        self.driver.execute_script("arguments[0].scrollIntoView();", element)
        WebDriverWait(self.driver, self.timeout).until(expected_conditions.element_to_be_clickable(element_locator))
        return element

    def scroll_to_element_use_element_itself(self, element):
        self.driver.execute_script("arguments[0].scrollIntoView();", element)
        WebDriverWait(self.driver, self.timeout).until(expected_conditions.element_to_be_clickable(element))

    def click_on_element(self, element_locator):
        self.scroll_to_element(element_locator)
        self.check_presence_of_element(element_locator).click()

    def input_data(self, element_locator, *args):
        self.check_presence_of_element(element_locator).click()
        self.check_presence_of_element(element_locator).send_keys(*args)

    def drag_and_drop_elements(self, element_locator_source, element_locator_destination):
        action = ActionChains(self.driver)
        source = self.check_presence_of_element(element_locator_source)
        destination = self.check_presence_of_element(element_locator_destination)
        action.drag_and_drop(source, destination).perform()

    def go_to_my_account(self):
        self.click_on_element(Bpl.MY_ACCOUNT_BUTTON)

    def go_to_constructor(self):
        self.click_on_element(Bpl.CONSTRUCTOR_BUTTON)

    def open_order_feed(self):
        self.click_on_element(Bpl.ORDER_FEED_BUTTON)




