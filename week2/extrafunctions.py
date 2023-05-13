# words = ['PYTHON', 'JoHN', 'chEEse', 'hAM', 'DOe']

# new_list = []

# for item in words :
#     new_item = item.upper()
#     new_list.append(new_item)
#     # if you orint inside loop it prints all instances 
#     # in order to only print the finl result print outside loop

# print(new_list)

# user_answer = "froggy"
# word_dict = {}
# for position, letter in enumerate(user_answer):
#     word_dict[letter]=[position]

# print(word_dict)


#                       FUNCTIONS 

# username = "John"
# my_name = "Tom"

# def say_hi(username):
#     print(f"Shalom {username + ' ' + my_name}")

# say_hi(username)

# function(parameters) Parameter - variables only used in the func
# value is passed when the func is called



# variable created inside a func is a local func
# "" created outside is global func - can be used externally
# weather = "windy"

# def create_information(user):
#     favourite_color = "Blue"
#     print(f"{user} likes {favourite_color}")
#     print(f"the weather is {weather}")

# create_information("Ahmed")

# def number(user_input):
#     if user_input % 2 == 0:
#         print("Number is even")
#     else:
#         print("Number is odd")

# number(11)

# Create a functions that receives a list of numbers, and check if each number is even or odd

# def list_number(user_list):
#     for number in user_list:
#         if number % 2 == 0:
#             print("Number is even")
#         else:
#             print("Number is odd")

# list_number([2, 3, 4, 5, 6])
        
# To print the number 
 
#                           FUNCTION PARAMETERS 

# def add_numbers(a, b, operation):
    # passing a value to the parameter makes it executable on default 
    # unless condition set 
    # e.g def list_number(a, b, operation = "plus")
#     if operation == "plus":
#         total = a + b
#     elif operation == "minus":
#         total = a - b
#     sum = a + b
#     print(sum)

# add_numbers(3,5, "minus")



# def list_number(user_list):

#     for number in user_list:
#         if number % 2 == 0:
#             print(f"{user_list} is even")
#         else:
#             print(f"{user_list} is odd")

# list_number([2,4,5])

# Running code works from Visual_Studio, not terminal 

# When using input - split() the user input into a list to iterate over it

# def square_root(user_input):
#     root = (2 * 50 * user_input)/30
#     return root

# square_root(25)


# def get_total():
#     prices = [20, 34, 44, 54]
#     total = 0
#     for item in prices:
#         total += item
#     return total # Return Gives value to the func
    
# my_total = get_total()

# print(my_total)

# def get_username():
#     my_name = "Binyamin"
#     return my_name


# def get_lastname():
#     my_lastname = "Marot"
#     return my_lastname

# def get_fullname():
#     first = get_username()
#     last = get_lastname()
#     fullname = f"{first} {last}"
#     return fullname

# full_name = get_fullname()
# print(full_name )

# same as 
# print(get_fullname())

vowels = ['a', 'e', 'i', 'o', 'u']

def super_vowels(user_input):
    new_word = ''
    for letter in user_input:
        if letter in vowels:
            new_word += letter.upper()
            # return new_word
        else:
            new_word += letter.lower()
            # return new_word
    return new_word
    
new_sentence = super_vowels("anabelle")
print(new_sentence)
#Code doesn't work as desired 

