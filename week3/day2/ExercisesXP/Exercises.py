
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
        self_score = self.run_speed() * self.weight
        other_score = other_dog.run_speed() * other_dog.weight 
        
        if self.score > other_dog.score:
            return f'{self.name} won the fight!'
        else:
            return f'{other_dog.name} won the fight!'
        

    
        

# #############################################################

# EXERCISE 3 : DOGS DOMESTICATED

# class Dog:

from Exercises import Dog 

PetDog = Dog()

class PetDog:
    def __init__(self, name, age, weight):
        super().__init__(name, age, weight)    
        self.trained = False

    def train(self):
        dog_bark = self.bark()
        self.trained = True
        print(dog_bark)

    def play(self, *args):
        dog_names = ', '.join([dog.name for dog in args])
        print(f"{dog_names} all play together.")

    def do_a_trick(self):
        tricks = [
            f"{self.name} does a barrel roll",
            f"{self.name} stands on his back legs",
            f"{self.name} shakes your hand",
            f"{self.name} plays dead."
        ]

        if self.trained:
            print(random.choice(tricks))
        else:
            print("The dog is not trained yet!")
        
    
