class Farm:
    def __init__(self, name):
        self.name = name
        self.animals = {}
    
    def add_animal(self, animal_type, quantity=1):
        if animal_type in self.animals:
            self.animals[animal_type] += quantity
        else:
            self.animals[animal_type] = quantity
    
    def get_info(self):
        info = "{}'s farm\n\n".format(self.name)
        for animal, quantity in sorted(self.animals.items()):
            info += "{:<10}: {:<2}\n".format(animal, quantity)
        info += "\nE-I-E-I-0!"
        return info

macdonald = Farm("McDonald")
macdonald.add_animal('cow', 5)

macdonald.add_animal('sheep')
macdonald.add_animal('sheep')
macdonald.add_animal('goat', 12)
print(macdonald.get_info())

class Farm:
    def __init__(self, name):
        self.name = name
        self.animals = {}
    
    def add_animal(self, animal_type, quantity=1):
        if animal_type in self.animals:
            self.animals[animal_type] += quantity
        else:
            self.animals[animal_type] = quantity
    
    def get_animal_types(self):
        return sorted(self.animals.keys())
    
    def get_info(self):
        info = "{}'s farm\n\n".format(self.name)
        for animal, quantity in sorted(self.animals.items()):
            info += "{:<10}: {:<2}\n".format(animal, quantity)
        info += "\nE-I-E-I-0!"
        return info
    
    def get_short_info(self):
        animal_types = ', '.join(self.get_animal_types())
        return "{}'s farm has {}.".format(self.name, animal_types)
