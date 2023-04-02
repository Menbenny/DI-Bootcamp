class Cat:
    def __init__(self, cat_name, cat_age):
        self.name = cat_name
        self.age = cat_age

    # Instances 

cat1 = Cat("maya", 5)
cat2 = Cat("Sali", 7)
cat3 = Cat("Miya", 9)

    # 

def find_oldest_cat(cat_list):
    oldest_cat = None
    for cat in cat_list:
        if oldest_cat is None or cat.age > oldest_cat.age:
            oldest_cat = cat
    return oldest_cat

oldest_cat = find_oldest_cat([cat1, cat2, cat3])

print(f"The oldest cat is {oldest_cat.name}, and is {oldest_cat.age} years old.")
