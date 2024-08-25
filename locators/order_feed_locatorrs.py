from selenium.webdriver.common.by import By


class OrderFeedLocators:
    ORDER_FEED_HEADER = [By.XPATH, "//h1[text()='Лента заказов']"]
    ALL_ORDERS = [By.XPATH, "//ul/li/a[@class='OrderHistory_link__1iNby']"]
    ORDER_POP_UP = [By.XPATH, "//div[@class='Modal_orderBox__1xWdi Modal_modal__contentBox__sCy8X p-10']/p[@class='text text_type_digits-default mb-10 mt-5']"]
    ORDERS_NUMBER_ALL_TIME = [By.CSS_SELECTOR, "div div.undefined.mb-15 p.OrderFeed_number__2MbrQ.text.text_type_digits-large"]
    ORDERS_NUMBER_ALL_TODAY = [By.CSS_SELECTOR, "div div:nth-child(3) p.OrderFeed_number__2MbrQ.text.text_type_digits-large"]
    ORDERS_IN_PROGRESS = [By.CSS_SELECTOR, "ul.OrderFeed_orderListReady__1YFem.OrderFeed_orderList__cBvyi li.text.text_type_digits-default.mb-2"]

