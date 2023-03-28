family = {"rick": 43, 'beth': 13, 'morty': 5, 'summer': 8}


total_cost = 0
for name, age in family.items():
    if age < 3:
        cost = 0
    elif age >= 3 and age <= 12:
        cost = 10
    else:
        cost = 15
    print(f"{name}: ${cost}.")
    total_cost += cost


print(f"Total cost: ${total_cost}.")

# family = {}

# while True:
#     name = input("Enter family member's name (or 'finish' to finish): ")
#     if name == 'finish':
#         break
#     age = int(input("Enter family member's age: "))
#     family[name] = age

# total_cost = 0
# for name, age in family.items():
#     if age < 3:
#         cost = 0
#     elif age >= 3 and age <= 12:
#         cost = 10
#     else:
#         cost = 15
#     print(f"{name} has to pay ${cost}.")
#     total_cost += cost


# print(f"The family's total cost is ${total_cost}.")
