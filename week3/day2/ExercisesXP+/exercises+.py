##########################################################

# EXERCISE 1 : FAMILY  

class Family:
    def __init__(self, last_name, members):
        self.last_name = last_name 
        self.members = members 

    def born(self, **kwargs):
        kwargs['is_child'] = True
        self.members.append(kwargs)
        print(f"Congratulations, {kwargs['name']} was born!")

    def is_18(self, name):
        for member in self.members:
            if member['name'] == name:
                return member['age'] >= 18
        return False
    
    def family_presentation(self):
        print(f"The {self.last_name} family members are: ")
        for member in self.members:
            print(f" - {member['name']}")

# initial_members = [
#     {'name':'Michael','age':35,'gender':'Male','is_child':False},
#     {'name':'Sarah','age':32,'gender':'Female','is_child':False}
# ]
# my_family = Family('Johnson', initial_members)

        
 ##########################################################
  
 # EXERCISE 2 : THEINCREDIBLES FAMILY
  
class TheIncredibles(Family):

    def __init__(self, last_name, members):
        super().__init__(last_name, members)

    def use_power(self, name):
        for member in self.members:
            if member['name'] == name:
                if member['age'] >= 18:
                    print(f"{name}'s power is: {member['power']}")
                else:
                    raise Exception(f"{name} is not over 18 years old and cannot use this power.")

    def incredible_presentaion(self):
        super().family_presentation()
        for member in self.members:
            print(f"- {member['incredible_name']}: {member['power']}")

# initial_members = [
#     {'name':'Michael','age':35,'gender':'Male','is_child':False,'power': 'fly','incredible_name':'MikeFly'},
#     {'name':'Sarah','age':32,'gender':'Female','is_child':False,'power': 'read minds','incredible_name':'SuperWoman'}
# ]
# my_incredibles = TheIncredibles('Parr', initial_members)
            
            
                    
    