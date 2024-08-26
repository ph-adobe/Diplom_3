import random
from faker import Faker
from locators.ingredients_locators import Ingredients


class GenerateUserData:
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


class GenerateOrderData:
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
