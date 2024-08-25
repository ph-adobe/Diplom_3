import pytest
from api_usage import Users, Orders
from pages.login_page import LoginPage
from locators.main_page_locators import MainPageLocators as Mpl
from data_for_tests import UserData, OrderData
from factory import WebDriverFactory
from urls import PageURL as Url


@pytest.fixture(params=["chrome", "firefox"])
def driver(request):
    driver = WebDriverFactory.get_web_driver(request.param)
    driver.get(Url.MAIN_PAGE)
    yield driver
    driver.quit()


@pytest.fixture
def login_data():
    registration_data = UserData.generate_registration_data()
    api_users = Users()
    api_users.register_new_user(registration_data)
    login_data = UserData.return_login_data(registration_data)
    yield login_data
    api_users.delete_user(login_data)


@pytest.fixture
def login_user(login_data, driver):
    login_page = LoginPage(driver)
    login_page.login(login_data)


@pytest.fixture
def login_data_user_with_orders(login_data):
    login_data_user_with_orders = login_data
    api_orders = Orders()
    for _ in range(2):
        api_orders.make_order(OrderData.ingredients, login_data)

    return login_data_user_with_orders


@pytest.fixture
def login_user_with_orders(login_data_user_with_orders, driver):
    login_page = LoginPage(driver)
    login_page.login(login_data_user_with_orders)