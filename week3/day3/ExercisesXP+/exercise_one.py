# import func  

# ########################################################

# # EXERCISE 2: Random Module

# def func100(num):
#     num = 0 > 101

#     def __int__(num):
#         while True: 
#             return "Number accepted"
            
# ########################################################

# # EXERCISE 3: String Module

# # random_str = 'a' 

# import random
# import string 

# my_string = '' .join(random.choices(string.ascii_lowercase + string.ascii_uppercase, k=5))

# ########################################################

# # EXERCISE 4: Current Date

# import datetime

# x = datetime.datetime.now()
# print(x)

# ########################################################

# # EXERCISE 5: Amount Of Time Left Until January 1st

# from datetime import dateime 

# def time_left():
#     now = datetime.now()
#     new_year = datetime(now.year +1, 1, 1)
#     time_left = new_year - now 
#     print(f'Time left intil New year: {time_left}')

# ########################################################

# # EXERCISE 6: Birthday And Minutes 

# from datetime import datetime

# def minutes(birthdate):
#     birth_datetime = datetime.strptime(birthdate, '%Y-%m-%d')
#     now_datetime =datetime.now()
#     time_lived =now_datetime - birth_datetime
#     minutes = int(time_lived.total_seconds() / 60)
#     print(f"You've lived {minutes:,} minutes so far in your life!")

# ########################################################

# #  EXERCISE 7: Upcoming Holiday

from datetime import datetime

# x = dateime.dateime.now()
# print(x)

def holiday():

    holiday_datetime = datetime(2023, 4, 15, 0, 0, 0)
    holiday_name = "Python Day"

    now_datetime = datetime.now()

    time_left = holiday_datetime - now_datetime

    days = time_left.days
    seconds = time_left.seconds
    hours = seconds // 3600
    minutes = (seconds % 3600) // 60
    seconds = (seconds % 3600) % 60
    time_left_str = f"{days} days and {hours:02d}:{minutes:02d}:{seconds:02d} hours"

    print(f"Today's date is {now_datetime.date()}")
    print(f"The next upcoming holiday is {holiday_name} in {time_left_str}.")

########################################################

#  EXERCISE 8: How Old Are You On Jupiter?

def calculate_age(age_seconds):

    earth_year = 365.35 * 24 * 60 * 60
    mercury_year = 0.2408467 * earth_year
    venus_year = 0.61519726 * earth_year
    mars_year = 1.8808158 * earth_year
    jupiter_year = 11.862615 * earth_year
    saturn_year = 29.447498 * earth_year 
    uranus_year = 84.016846 * earth_year
    neptune_year = 164.79132 * earth_year 

    age_earth_years = age_seconds / earth_year 
    age_mercury_years = age_seconds / mercury_year 
    age_venus_years = age_seconds / venus_year 
    age_mars_years = age_seconds / mars_year
    age_jupiter_years = age_seconds /jupiter_year
    age_saturn_years = age_seconds / saturn_year
    age_uranus_years = age_seconds / uranus_year
    age_neptune_years = age_seconds / neptune_year 

    print(f"You are {age_earth_years:.2f} Earth-years old.")
    print(f"You are {age_mercury_years:.2f} Mercury-years old.")
    print(f"You are {age_venus_years:.2f} Venus-years old.")
    print(f"You are {age_mars_years:.2f} Mars-years old.")
    print(f"You are {age_jupiter_years:.2f} Jupiter-years old.")
    print(f"You are {age_saturn_years:.2f} Saturn-years old.")
    print(f"You are {age_uranus_years:.2f} Uranus-years old.")
    print(f"You are {age_neptune_years:.2f} Neptune-years old.")

#########################################################

# EXERCISE 9: Faker Module 

from faker import Faker 

fake = Faker()

users = []

def add_user():
    name = fake.name()
    address = fake.address()
    language_code = fake.language_code()

    new_user = {
        "name" : name,
        "address" : address,
        "language_code" : language_code
    }

    users.append(new_user)

    