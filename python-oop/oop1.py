# A class is a simple blueprint how an object should look like and how it will function
# use class keyword and name should be cammelcase

# this is a class without anything

# class Microwave:
#     ...

# self is the actial instance of the class, you can use anyname its not just "self" you can use "this" or anything

class Microwave:
    def __init__(self, brand: str, power_rating: str) -> None:
        self.brand = brand
        self.power_rating = power_rating


smeg: Microwave = Microwave('Smeg', 'B')

print(smeg)
print(smeg.brand)
print(smeg.power_rating)

bosch: Microwave = Microwave("Bosch", "C")

print(bosch.brand)
print(bosch.power_rating)

