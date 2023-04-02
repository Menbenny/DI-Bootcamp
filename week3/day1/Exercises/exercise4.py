class Zoo:
    def __init__(self, zoo_name):
        self.name = zoo_name
        self.animals = []
        
    def add_animal(self, new_animal):
        if new_animal not in self.animals:
            self.animals.append(new_animal)
            print(f"{new_animal} has been added to the zoo!")
        else:
            print(f"{new_animal} is already in the zoo!")
    
    def get_animals(self):
        print("The animals in the zoo are:")
        for animal in self.animals:
            print(animal)
    
    def sell_animal(self, animal_sold):
        if animal_sold in self.animals:
            self.animals.remove(animal_sold)
            print(f"{animal_sold} has been sold from the zoo.")
        else:
            print(f"{animal_sold} is not in the zoo!")
    
    def sort_animals(self):
        animal_dict = {}
        for animal in self.animals:
            if animal[0] not in animal_dict:
                animal_dict[animal[0]] = [animal]
            else:
                animal_dict[animal[0]].append(animal)
        sorted_dict = dict(sorted(animal_dict.items()))
        print("The animals in the zoo sorted by their first letter are:")
        for key, value in sorted_dict.items():
            if len(value) == 1:
                print(f"{key}: {value[0]}")
            else:
                print(f"{key}: {value}")
    
    def get_groups(self):
        animal_dict = {}
        for animal in self.animals:
            if animal[0] not in animal_dict:
                animal_dict[animal[0]] = [animal]
            else:
                animal_dict[animal[0]].append(animal)
        print("The animals in the zoo grouped by their first letter are:")
        for key, value in animal_dict.items():
            print(f"{key}: {value}")
