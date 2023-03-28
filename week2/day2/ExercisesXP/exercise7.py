favourite_fruits = input('What is your favourite fruit(s)? (If multiple, add space!)')

# print(favourite_fruits)


list = favourite_fruits.split(',')

print(list)

f = input('Name any fruit: ')

while f == favourite_fruits:
    print('You chose one your favourite fruits! Enjoy!')
else:
    print('You chose a new fruit. I hope you enjoy!')