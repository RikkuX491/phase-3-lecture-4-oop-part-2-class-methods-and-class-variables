import ipdb

class Animal:

    all = []
    
    def __init__(self, name, age):
        self.name = name
        self.age = age
        Animal.all.append(self)

    def make_animal_sound(self):
        print("Animal sounds!")

    @classmethod
    def get_all_animal_names(cls):
        return [animal.name for animal in cls.all]