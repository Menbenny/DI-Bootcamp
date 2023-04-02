class Dog:
    def __init__(self, name, height):
        self.name = name
        self.height = height

    def bark(self):
        print(f"{self.name} goes woof!")

    def jump(self):
        print(f"{self.name} jumps {self.height*2} cm high!")

#  Funtions Instances 

        # 

davids_dog = Dog("RAJi", 50)
print(f"David's dog's name is {davids_dog.name} and height is {davids_dog.height}cm.")
davids_dog.bark()
davids_dog.jump()

Sabeen_dog = Dog("Kulkulkan", 20)
print(f"Sabeen's dog's name is {Sabeen_dog.name} and height is {Sabeen_dog.height}cm")
Sabeen_dog.bark()
Sabeen_dog.jump()

if davids_dog.height > Sabeen_dog.height:
    print(f"{davids_dog.name} is bigger.")
elif Sabeen_dog.height > davids_dog.height:
    print(f"{Sabeen_dog.name} is bigger.")
else:
    print("Both dogs are the same height.")