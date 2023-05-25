import ipdb
from animal import *

class Dog(Animal):

    all = []

    def __init__(self, name, age, bark_volume):
        super().__init__(name, age)
        self.bark_volume = bark_volume
        Dog.all.append(self)
    
    def make_animal_sound(self):
        animal_sound = "Bark"
        for i in range(self.bark_volume):
            animal_sound += "!"
        print(animal_sound)

    def get_name(self):
        return self._name
    
    def set_name(self, name):
        if(not hasattr(self, "name")):
            self._name = name
        else:
            raise Exception("Cannot change the name of a dog!")

    name = property(get_name, set_name)