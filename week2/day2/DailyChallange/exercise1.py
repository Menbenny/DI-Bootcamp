number = "n"
length = "l"

n = int(input("Enter a number: "))
l = int(input("Enter the desired length of the list: "))

multiples = []
count = 1

while len(multiples) < l:
    multiples.append(n * count)
    count += 1

print(multiples)