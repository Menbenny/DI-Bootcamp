# class vehicle :
#     def __init__(self, vehicle_type, vehicle_model, vehicle_color, model_year) :
#         self.type = vehicle_type
#         self.model = vehicle_model
#         self.color = vehicle_color
#         self.year = model_year
#         self.current_location = 0
    
#                 # -- METHOD --
#     def move(self) :
#         self.current_location += 10

# vehicle_1 = vehicle("Truck", "Scania", "Black", 2020)

# # print(vehicle_1.type)

# Exercise 1
# Create a Employee class, With the attributes : firstname, lastname, age, job, salary
# Create 2 users object and display their attribute
# Lea Smith 30 years old developer 30000
# David Schartz 20 years old project manager 20000
# Add those methods to the class
# get_fullname(self) : that return the firstname + lastname
# happy_birthday(self) : that return the age incremented by one
# get_promotion(self, promotion_amount) : that increment the salary of the user by the promotion
# Call all the methods

# class Employee:
#     def __init__(self, firstname, lastname, age, job, salary):
#         self.firstname = firstname
#         self.lastname = lastname
#         self.age = age
#         self.job = job
#         self.salary = salary
    
#     def get_fullname(self):
#             return self.firstname + " " + self.lastname

#     def happy_birthday(self):
#             self.age += 1

#     def get_promotion(self, promotion_amount):
#                 self.salary += promotion_amount

#     def __str__(self):
#         return f"{self.firstname} {self.lastname} is {self.age} years old and works as {self.job}"
    
# lea = Employee("Lea", "Smith", 30, "Developer", 30000)
# david = Employee("David", "Schartz", 20, "Project Manager", 20000)

# print(lea)
# print(david)

# lea.happy_birthday()
# lea.get_promotion(10000)

# print(lea)
# print(david) 
# print(lea.get_fullname())
# print(david.get_fullname())
# print(lea.__str__())
# print(david.__str__())
# Exercise 2
# Create a Vehicle class, With the attributes : brand, model, color, year
# Create 2 vehicles object and display their attribute
# Truck Scania Black 2020



# from random import random

# class circle:
#     def __init__(self, radius):
#         self.radius = radius
#         def area(self):
#             return 3.14 * self.radius * self.radius
    

#######################################################################

# Exercise 1 : Geometry
# Instructions
# Write a class called Circle that receives a radius as an argument (default is 1.0).
# Write two instance methods to compute perimeter and area.
# Write a method that prints the geometrical definition of a circle.

# class circle:
#     def __init__(self, radius = 1.0):
#         self.radius = radius
        
#     def perimeter(self):
#         return 2 * 3.14 * self.radius
    
#     def area(self):
#         return 3.14 * self.radius * self.radius
    
#     def print_geometrical_definition(self):
#         print(f"A circle with radius {self.radius} has a perimeter of {self.perimeter()} and an area of {self.area()}")
    
# c = circle()
# c.print_geometrical_definition()
# c.radius = 2
# c.print_geometrical_definition()
# c.radius = 3

####################################################################

# Exercise 2
# Create a Developer class, that inherits from the Employee class With the attributes : firstname, lastname, age, job is developer as default, salary is 15000 by default, coding skills (a list by default)
# Create 2 developer object and display his attribute
# Tom Cruiz 30 years old Python
# Angelina Jolie 23 years old Javascript
# Add those methods to the class
# add_skills(self, *skills)
# coding(self) : print a nice sentence with the coding language
# coding_with_partner(self, other_developer) : print a nice sentence with the name of both developers, and their coding language
# override the get_promotion(self, promotion_amount) : that multiplies the salary of the user by the promotion
# Call all the methods, also those from the Employee Class

class developer:
    def __init__(self, firstname, lastname, age, job, salary, skills = []):
        self.firstname = firstname
        self.lastname = lastname
        self.age = age
        self.job = job
        self.salary = salary
        


