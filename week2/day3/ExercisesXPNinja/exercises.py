cars_list = ("Volkswagen, Toyota, Ford Motor, Honda, Chevrolet")

def new_list():
    return cars_list.split()

def manufacturers_number():
    return len(cars_list)

print(f'The number of companies is {manufacturers_number}')
    

