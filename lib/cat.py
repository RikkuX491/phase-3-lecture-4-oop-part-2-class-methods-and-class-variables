import ipdb
from animal import *

class Cat(Animal):

    all = []
    
    def __init__(self, name, age, meow_volume):
        super().__init__(name, age)
        self.meow_volume = meow_volume
        self.id = len(Cat.all) + 1
        Cat.all.append(self)

    def make_sound(self):
        print(f"MEOW{'!' * self.meow_volume}")

    @classmethod
    def get_info_for_all_cats(cls):
        return [f'Cat # {cat.id}: {cat.name} is {cat.age} years old.' for cat in cls.all]