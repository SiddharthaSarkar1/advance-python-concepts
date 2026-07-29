from abc import ABCMeta, abstractstaticmethod

class IPerson(metaclass=ABCMeta):

    @abstractstaticmethod
    def print_data():
        """ Implement it in child class """


class PersonSingleton(IPerson):

    __instance = None

    @staticmethod
    def get_instance():
        if PersonSingleton.__instance is None:
            PersonSingleton("Default name", 0)
        return PersonSingleton.__instance

    def __init__(self, name, age):
        self.name = name
        self.age = age
        if PersonSingleton.__instance is not None:
            raise Exception("This class is a singleton!")
        else:
            PersonSingleton.__instance = self

    @staticmethod
    def print_data():
        print(f"Name: {PersonSingleton.__instance.name}, Age: {PersonSingleton.__instance.age}")



p = PersonSingleton("Mike", 30)
p.print_data()

