# exercise 1 gold XP

# list_a = [1, 2, 3, 4, 5]
# list_b = ["Me", "You", "Them", "Us", "They"]

# lists = zip(str(list_a), list_b)

# print(lists)




#  exercise 2

# numbers = range(1500, 2501) # In Range NB end number/index always one plus

# for num in numbers:
#     if num % 5 == 0 and num & 7 == 0:
#         print(num)




# exercise 3

# names = ['Samus', 'Cortana', 'V', 'Link', 'Mario', 'Cortana', 'Samus']

# user_name = input("Please enter your name: ")

# if user_name in names:
#         index = names.index(user_name)
#         print(f'{index}')
# else:
#     print("name doesn't match the list")
    



# Exercise 4

# user_input = input('Enter 3 different numbers: ')
# numbers = user_input.split()
 
# for num in numbers:
#       if num == max(user_input):
#             print(num)

# print(num)


# def user_name():
#     user_name = input("Please enter your name: ")  
#     if  user_name in names:
        
# print(names.index(user_name))




# Exercise 5

# Create a string of all the letters in the alphabet
# Loop over each letter and print a message that contains the letter and whether its a vowel or a consonant.

alphabet = ("abcdefghijklmnopqrstuvwxyz")
vowels=0
consonant=0



for letter in alphabet:
    if letter in 'aeiou':
        print(f"letter {letter} is a vowel")
    else:
        print(f"letter {letter} is a consonant")
          









