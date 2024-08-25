import allure
import json
import requests

URL = "https://stellarburgers.nomoreparties.site"
create_user_path = "/api/auth/register"
users_path = "/api/auth/user"
login_path = "/api/auth/login"
orders_path = "/api/orders"


class Users:
    @allure.step("API: user registration")
    def register_new_user(self, registration_data):
        payload = json.dumps(registration_data)
        response = requests.post(
            f"{URL}{create_user_path}",
            data=payload,
            headers={
                "Content-type": "application/json"
            }
        )
        return response.status_code, response.json()

    @allure.step("API: user login")
    def login(self, login_data):
        payload = json.dumps(login_data)
        response = requests.post(
            f"{URL}{login_path}",
            data=payload,
            headers={
                "Content-type": "application/json"
            }
        )
        return response.status_code, response.json()

    @allure.step("API: get access token")
    def get_access_token(self, login_data):
        status_code, response_body = self.login(login_data)
        if status_code == 200:
            access_token = response_body["accessToken"]
            return access_token
        else:
            print("Что-то пошло не так, не удалось получить accessToken.")

    @allure.step("API: delete user")
    def delete_user(self, login_data):
        access_token = self.get_access_token(login_data)
        requests.delete(
            f"{URL}{users_path}",
            headers={
                "Content-type": "application/json",
                "Authorization": access_token
            }
        )


class Orders:
    user = Users()

    @allure.step("API: make order")
    def make_order(self, ingredients, login_data):
        access_token = self.user.get_access_token(login_data)
        order_data = {"ingredients": ingredients}
        payload = json.dumps(order_data)

        headers = {
            "Content-type": "application/json",
            "Authorization": access_token
        }

        response = requests.post(
            f"{URL}{orders_path}",
            data=payload,
            headers=headers
        )
        return response.status_code, response.json()
