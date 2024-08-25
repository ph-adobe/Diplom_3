import random
from faker import Faker
from selenium.webdriver.common.by import By

from locators.ingredients_locators import Ingredients


class UserData:
    @staticmethod
    def generate_registration_data():
        fake = Faker()
        reg_data = {
            "name": fake.user_name(),
            "email": fake.email(),
            "password": fake.password()
        }
        return reg_data

    @staticmethod
    def return_login_data(registration_data):
        login_data = {
            "email": registration_data["email"],
            "password": registration_data["password"]
        }
        return login_data

    @staticmethod
    def return_email():
        fake = Faker()
        return fake.email()

    @staticmethod
    def return_password():
        fake = Faker()
        return fake.password()


class OrderData:
    fake = Faker()

    buns = [
        "61c0c5a71d1f82001bdaaa6d",
        "61c0c5a71d1f82001bdaaa6c"
    ]

    sauces = [
        "61c0c5a71d1f82001bdaaa72",
        "61c0c5a71d1f82001bdaaa73",
        "61c0c5a71d1f82001bdaaa74",
        "61c0c5a71d1f82001bdaaa75"
    ]
    fillings = [
        "61c0c5a71d1f82001bdaaa6f",
        "61c0c5a71d1f82001bdaaa70",
        "61c0c5a71d1f82001bdaaa71",
        "61c0c5a71d1f82001bdaaa6e",
        "61c0c5a71d1f82001bdaaa76",
        "61c0c5a71d1f82001bdaaa77",
        "61c0c5a71d1f82001bdaaa78",
        "61c0c5a71d1f82001bdaaa7a"
    ]

    ingredients = [
        fake.random_element(buns),
        *fake.random_elements(sauces, random.randint(0, 4), True),
        *fake.random_elements(fillings, random.randint(0, 8), True)
    ]

    @staticmethod
    def return_random_ingredient():
        ingredients = [Ingredients.SAUCES, Ingredients.FILLINGS]
        random_ingredient_group = random.choice(ingredients)
        random_ingredient = random.choice(random_ingredient_group)[0]
        return random_ingredient

    @staticmethod
    def return_random_ingredient_with_counter():
        ingredients = [Ingredients.SAUCES, Ingredients.FILLINGS]
        random_ingredient_group = random.choice(ingredients)
        random_ingredient = random.choice(random_ingredient_group)
        random_ingredient_locator = random_ingredient[0]
        random_ingredient_counter = random_ingredient[1]
        return random_ingredient_locator, random_ingredient_counter

    @staticmethod
    def return_ingredients_to_order():
        fake = Faker()

        ingredients = [
            fake.random_element(Ingredients.BUNS),
            fake.random_element(Ingredients.SAUCES)[0],
            fake.random_element(Ingredients.FILLINGS)[0]
         ]
        return ingredients

print(OrderData.return_random_ingredient_with_counter())