#                   Exercises XP GOLD - week2 day2

# list1 = ['ben', 'jay']
# list2 = ['Mariam', 'Ofri']

# for x in list2:
#     list1.append(x)
#     print(list1)

# range = int(1500 <= 2500)

# while range // 5 == True or range // 7 == True:
#     print(range)

# for i in range(1500, 2501):
#     if i % 5 == 0 or i % 7 == 0:
#         print(i)
d = ('%y/%m/%d')
birthdays = {
    'Jay': '1996/05/18)',
    'Mia': '1977/02/19)',
    'Yon': '1992/12/23)',
    'Ian': '1998/04/17)',
    'Paul': '1990/09/27)'
}



print(birthdays.keys())

new_name = input("Enter a new name: ")
new_birthday = input("Date of birth 'YYYY/MM/DD': ")

birthdays[new_name] = new_birthday

i = input("Please enter a name: ")

birthday = birthdays.get(i)

if birthday:
    
    print(f'The birthdate for {i} is: {birthday}')

else:
    print(f'Sorry, there is no corresponding information for {i}')

