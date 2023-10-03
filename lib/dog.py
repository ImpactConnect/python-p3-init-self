#!/usr/bin/env python3

class Dog:
    def __init__(self, name, breed='Mutt'):
        self.name = name
        self.breed = breed


    def bark(self):
        print("Woof!")
        
    # def breed(self, breed):
    #     self.breed = breed

fido = Dog("Fido")
fido.name
fido.breed
