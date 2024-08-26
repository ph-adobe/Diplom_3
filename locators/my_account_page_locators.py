from selenium.webdriver.common.by import By


class MyAccountPageLocators:
    PROFILE_HEADER = [By.XPATH, "//a[@href='/account/profile']"]
    LOGOUT_BUTTON = [By.XPATH, "//button[text()='Выход']"]
    PROFILE_USER_EMAIL = [By.XPATH, "//label[text()='Логин']"]
    ORDER_HISTORY = [By.XPATH, "//a[@href='/account/order-history']"]
    MY_ORDERS = [By.XPATH, "//ul/li/a[@class='OrderHistory_link__1iNby']"]
