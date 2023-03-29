import random

def number_game():
    random_number = random.randint(1, 100)

    while True:
        guess = int(input("Guess a number between 1 and 100: "))
        if guess == random_number:
            print("Congratulations! You guessed the number " + str(random_number) + " correctly!")
            break
        else:
            print("Sorry, you guessed the number " + str(guess) + ", but the correct number was " + str(random_number) + ".")
number_game()
