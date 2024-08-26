import random
from faker import Faker


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
