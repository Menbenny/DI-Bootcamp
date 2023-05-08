# list1 = [5, 10, 15, 20, 25, 50, 20]
# list1[3] = 200
# print(list1[3])

# BEST PRACTICE

# list1 = [5, 10, 15, 20, 25, 50, 20]
# position = list1.index(20)
# list1[position] = 200



# a_tuple = (10, 20, 30, 40)
# a_tuple = 10, 20, 30, 40
# a_tuple = "a", "b", "c", "d", "e"


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
names = ['Samus', 'Cortana', 'V', 'Link', 'Mario', 'Cortana', 'Samus']

user_name = input("Please enter your name: ")

if user_name in names:
        index = names.index(user_name)
        print(f'{index}')
else:
    print("name doesn't match the list")
    













# def user_name():
#     user_name = input("Please enter your name: ")  
#     if  user_name in names:
        
# print(names.index(user_name))


