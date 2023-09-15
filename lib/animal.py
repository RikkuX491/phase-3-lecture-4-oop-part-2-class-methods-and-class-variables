import ipdb

class Animal:

    all = []
    
    def __init__(self, name, age):
        self.name = name
        self.age = age
        Animal.all.append(self)
    
    def make_sound(self):
        print('Animal sounds!!! :D')