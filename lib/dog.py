import ipdb
from animal import *

class Dog(Animal):

    all = []
    
    def __init__(self, name, age, bark_volume):
        super().__init__(name, age)
        self.bark_volume = bark_volume
        self.id = len(Dog.all) + 1
        Dog.all.append(self)

    def make_sound(self):
        print(f"BARK{'!' * self.bark_volume}")

    @classmethod
    def get_info_for_all_dogs(cls):
        return [f'Dog # {dog.id}: {dog.name} is {dog.age} years old.' for dog in cls.all]