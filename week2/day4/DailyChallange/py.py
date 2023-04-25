n = input("Enter a number between 1 and 100: ")
if int(n) < 100:
    print(n)
    print("Number accepted.")
if    int(n) % 3 == 0 and int(n) < 100:
    print("__FIZZ")
if int(n) % 5 == 0:
    print("__BUZZ")
elif int(n) > 100:
    print("Number declined.")
    


