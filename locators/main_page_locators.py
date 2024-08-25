from selenium.webdriver.common.by import By


class MainPageLocators:

    LOG_IN_BUTTON = [By.XPATH, "//button[text()='Войти в аккаунт']"]
    MY_ACCOUNT_BUTTON = [By.XPATH, "//p[text()='Личный Кабинет']"]
    MAKE_ORDER_BUTTON = [By.XPATH, "//button[text()='Оформить заказ']"]
    MAKE_BURGER_HEADER = [By.XPATH, "//h1[text()='Соберите бургер']"]
    INGREDIENT_DETAILS = [By.XPATH, "//h2[text()='Детали ингредиента']"]
    CLOSE_INGREDIENT_POPUP = [By.CLASS_NAME, "Modal_modal__close_modified__3V5XS.Modal_modal__close__TnseK"]
    TOP_BUN = [By.CLASS_NAME, "constructor-element.constructor-element_pos_top"]
    BOTTOM_BUN = [By.CLASS_NAME, "constructor-element.constructor-element_pos_top"]
    ORDER_ID = [By.CSS_SELECTOR, "div.Modal_modal__container__Wo2l_ div h2"]
    ORDER_POP_UP = [By.CSS_SELECTOR, "div div.Modal_modal__contentBox__sCy8X.pt-30.pb-30"]
    CLOSE_POPUP_ORDER = [By.CSS_SELECTOR, "div section.Modal_modal_opened__3ISw4.Modal_modal__P3_V5 button.Modal_modal__close_modified__3V5XS.Modal_modal__close__TnseK svg path"]
    STARTED_MAKE_YOUR_ORDER = [By.XPATH, "//p[text()='Ваш заказ начали готовить']"]
    TICK_ANIMATION = [By.CSS_SELECTOR, "div img[alt='tick animation']"]



