
# #############################################################

# EXERCISE 1 : PETS

class Pets():
    def __init__(self, animals):
        self.animals =animals 

    def walk(self):
        for animal in self.animals:
            print(animal.walk())

class Cat():
    is_lazy = True 

    def __init__(self, name, age):
        self.name = name 
        self.age = age

    def walk(self):
        return f'{self.name} is just walking around'
    
class Bengal(Cat):
    def sing(self, sounds):
        return f'{sounds}'    
    
class Chartreux(Cat):
    def sing(self, sounds):
        return f'{sounds}'    
        
class Siamese(Cat):
    def sing(self, sounds):        
        return f'{sounds}'

all_cats = [
    Bengal,
    Chartreux,
    Siamese
    ]

sara_pets = Pets(all_cats)

sara_pets.walk()

# #############################################################

# EXERCISE 2 : DOGS

class Dog:
    def __init__(self, name, age, weight):
        self.name = name 
        self.age = age
        self.weight = weight 
    
    def bark(self):
        return f'{self.name} is barking'
    
    def run_speed(self):
        return f'{self.weight/self.age*10}'
    
    def fight(self, other_dog):
        self.score = self.run_speed * self.weight
        other_dog.score = other_dog.run_speed * other_dog.weight 
        
        if 
    
        

