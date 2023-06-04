# def even():
#     for number in numbers:
#         if number % 2 ==0:
#             print(number "Even")
#         return number 

# numbers = [20, 31,45, 54,34, 23,34, 75]

# new_list = [number for numbers in numbers if number %2 ==0]
# print(new_list)

# List comprehension 
# To have a loop on one code(i.e for loop)

fruits = ["apples", "banana", "Pear"]

plural_fruits = [fruit +'s' for fruit in fruits]
print(plural_fruits)

# same as 
new_list = []
for fruit in fruits:
    new_list.append(fruit +'s')