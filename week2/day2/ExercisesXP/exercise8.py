toppings = []                     

topping_price = "tp"
tp = 2.5

while True:
    topping = input("Enter a pizza topping (enter 'quit' to stop): ")
    print('Topping will be added to your Pizza!')
    if topping == 'quit':
        break
        pass

        print(f"You ordered a pizza with the following toppings: {', '.join(toppings)}")
        print(f"The total price is: ${total:.2f}")


    else:
        toppings.append(topping)

total = 10 + len(topping) * tp

# print("You ordered a pizza with the following toppings:")
# print(", ".join(toppings))

print(f"You ordered a pizza with the following toppings: {', '.join(toppings)}") # .join converts list into string 
print(f"The total price is: ${total:.2f}")

