    

# ##########################################

# EXERCISE 1 : Built-In Functions 

# def Document():
#     """
#     The code prompts the user to enter an input. Input is
#     then convereted to an integer through the int function,
#     the absolute value of the integer is what is printed out.
#     """

# num_str = input("Enter a number: ")

# num_int = int(num_str)

# num_abs = abs(num_int)

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
            else:
                self.amount += other.amount 
                return self 
        else:
            self.amount += other
            return self 
        
c1 = Currency('dollar', 5)        
c2 = Currency('dollar', 10)
c3 = Currency('shekel', 1)
c4 = Currency('shekel', 10)

print(str(c1))
print(int(c1))
print(repr(c1))            
print(c1 + 5)
print(c1 + c2)
print(c1)
c1 += 5
print(c1)
c1 += c2
# print(c1)
# print(c1 + c3)

        
        