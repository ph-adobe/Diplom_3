from selenium.webdriver.common.by import By


class LoginPageLocators:
    INPUT_EMAIL = [By.XPATH, "//label[text()='Email']/../input"]
    INPUT_PASSWORD = [By.XPATH, "//label[text()='Пароль']/../input"]
    ENTRY_HEADER = [By.XPATH, "//h2[text()='Вход']"]
    ENTRY_BUTTON = [By.XPATH,  "//button[text()='Войти']"]
    RECOVERY_PASSWORD_LINK = [By.XPATH, "//a[@href='/forgot-password']"]
