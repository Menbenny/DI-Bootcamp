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

# alphabet = ("abcdefghijklmnopqrstuvwxyz")
# vowels=0
# consonant=0



# for letter in alphabet:
#     if letter in 'aeiou':
#         print(f"letter {letter} is a vowel")
#     else:
#         print(f"letter {letter} is a consonant")




# exercise 6

# code doesn't work properly

# words = [input("Enter seven words: ")] # HAD TO CONVERT TO A LIST FOR INDEX to be fully functional
# letter = input("Enter a single character: ")

# for word in words:
#     if letter in word:
#         index = word.index(letter)
#         print(f"{index}")
#         letter_index = word.index(letter)


# Exercise 7

# numbers = range(1, 1000001)
# print(min(numbers))
# print(max(numbers))
# print(sum(numbers))

# Exercise 8

# list = [input("Enter a sequence of numbers: ")]
# # list = list.split()
# list_tuple = tuple(list)
# print(list)
# print(list_tuple)

# Exercise 9 
import random 

user_input = input('Enter a any number between the numbers 1 to 9: ')

random_numbers = random.randint(1, 9)

for num in user_input:
    if num == random_numbers:
        print("Winner!")
    elif num == "quit":
        break   
        

 

# while user_input == random_numbers:
#     print("Good guess!")
# if user_input != 'quit':
#     print("Enter a number between 1 and 9 or the word 'quit' to quit.") 



# print(random_numbers)

# random_input = random.choice(user_input)





