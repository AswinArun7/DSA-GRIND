#INSTANCE METHOD
class Person:
    def __init__(self, name):
        self.name = name   # instance attribute
    
    def greet(self):       # instance method
        print("Hello, I'm ",self.name)

p = Person("Aswin")
p.greet()


#CLASS METHOD
class Person:
    species = "Human"
    
    @classmethod
    def get_species(cls):
        return cls.species
    
Person.get_species()


#STATIC METHOD
class Math:
    @staticmethod
    def add(a, b):
        return a + b

Math.add(3, 5)
