from selenium.webdriver.common.by import By


class BasePageLocators:
    CONSTRUCTOR_BUTTON = [By.XPATH, "//a[@href='/']/./p[text()='Конструктор']"]
    LOGO = [By.XPATH, "//div/a[@href='/']"]
    MY_ACCOUNT_BUTTON = [By.XPATH, "//p[text()='Личный Кабинет']"]
    ORDER_FEED_BUTTON = [By.XPATH, "//p[text()='Лента Заказов']"]