from selenium.webdriver.common.by import By


class ResetPassLocators:
    PASSWORD_RECOVERY_HEADER = [By.XPATH, "//h2[text()='Восстановление пароля']"]
    INPUT_CODE_FROM_EMAIL = [By.XPATH, "//label[text()='Введите код из письма']"]
    INPUT_PASSWORD = [By.XPATH, "//input[@name='Введите новый пароль']"]
    SAVE_BUTTON = [By.XPATH, "//button[text()='Сохранить']"]
    EYE_BUTTON = [By.CLASS_NAME, "input__icon.input__icon-action"]
    PASSWORD_FIELD = [By.XPATH, "//label[text()='Пароль']/../input"]
