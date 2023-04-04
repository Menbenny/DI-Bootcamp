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

class Car:
    def __init__(self, speed):
        self.speed = speed

    def __gt__(self, other_car):
        return self.speed > other_car.speed 

car1 = Car[200]
car2 = Car[300]
        