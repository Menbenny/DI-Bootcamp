total_cost = 0

while True:
    age = input("Enter the age of a person who wants a ticket (enter 'done' to calculate the total cost): ")
    if age == 'done':
        break
    elif int(age) < 3:
        total_cost += 0
    elif int(age) >= 3 and int(age) <= 12:
        total_cost += 10
    else:
        total_cost += 15

print(f"The total cost of the family's tickets is: ${total_cost}")

names = ['Alice', 'Bob', 'Charlie', 'David', 'Emily']
restricted_age_range = range(16, 22)

for name in names:
    age = int(input(f"{name}, enter your age: "))
    if age not in restricted_age_range:
        names.remove(name)

print(f"The following people are allowed to watch the movie: {', '.join(names)}")
