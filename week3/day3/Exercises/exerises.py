# static method are independent methods 
# does not require an output 
# no need for object with staticmethod
# like regular function Inside A Class

# class Useful:

#     @staticmethod
#     def capitalize_word(word: str):
#         return word.capitalized()
    
#     @staticmethod
#     def multiply_by_19(number:int):
#         return number * 19
    
# w = Useful

# ####################################

# class MyClass(object):
#     count = 0

#     def __init__(self, val):
#         self.val = val
#         MyClass.count += 1

#     def set_val(self, newval):
#         self.val = newval

#     def get_val(self):
#         return self.val

#     @classmethod
#     def get_count(cls):
#         return cls.count

# object_1 = MyClass(10)
# print("\nValue of object : %s" % object_1.get_val())
# print(MyClass.get_count())

# object_2 = MyClass(20)
# print("\nValue of object : %s" % object_2.get_val())
# print(MyClass.get_count())


# COMPARISON

# All operators have default dunder method - 

# class Car:
#     def __init__(self, speed):
#         self.speed = speed
# # gt- greater than 
#     def __gt__(self, other_car):
#         return self.speed > other_car.speed 
# # eq - equal
#     def __eq__(self, other_car):
#         return self.speed ==other_car.speed
# # +
#     def __add__(self, other_car):
#         return self.speed + other_car.speed
    
#     def __iadd__(self, other_car):
#         self.speed += other_car.speed 
#         return self 

# car1 = Car[200]
# car2 = Car[300]
        
# car1 += car2
# car1 = car2        

# ##########################################

# EXERCISE 1 : Built-In Functions 

def Document():
    """
    The code prompts the user to enter an input. Input is
    then convereted to an integer through the int function,
    the absolute value of the integer is what is printed out.
    """

num_str = input("Enter a number: ")

num_int = int(num_str)

num_abs = abs(num_int)

######################################

# EXERCISE 2: Currencies 

class Currency:
    def __init__(self, currency, amount):
        self.currency = currency 
        self.amount = amount 
          
    def __str__(self):
        return f"{self.amount} {self.currency}"
    
    def __init__(self):
        return self.amount
    
    def __repr__(self):
        return f"{self.amount} {self.currency}"
    
    def __add__(self, other):
        if isinstance(other, Currency):
            if self.currency !=other.currency:
                raise TypeError(f"Cannot add between Currency type {self.currency} and {other.currency}")
            return Currency(self.currency, self.amount + other.amount)
        else:
            return Currency(self.currency, self.amount + other)
        
    def __iadd__(self, other):
        if isinstance(other, Currency):
            if self.currency != other.currency:
                raise TypeError(f"Cannot add between Currency {self.currency} and {other.currency}")
            

        
        