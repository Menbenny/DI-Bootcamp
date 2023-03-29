import random

def get_random_temp(season):
    if season == "winter":
        return random.randint(-10, 16)
    elif season == "spring" or season == "autumn":
        return random.randint(0, 23)
    elif season == "summer":
        return random.randint(24, 40)
    else:
        return "Invalid season"


DEGREE_CELSIUS = "\u2103"

def main():
    season = input("Enter a season (summer, autumn, winter, spring): ")
    temp = get_random_temp(season)
    if type(temp) == int:
        print(f"The temperature is {temp} {DEGREE_CELSIUS}.")
        if temp < 0:
            print("Brrr, that's freezing! Wear some extra layers today.")
        elif temp < 16:
            print("Quite chilly! Don't forget your coat.")
        elif temp < 24:
            print("The temperature is moderate. Enjoy your day!")
        elif temp < 32:
            print("It's getting warm. Stay hydrated.")
        else:
            print("It's very hot outside. Stay cool and take care of yourself.")
    else:
        print(temp)


main()
