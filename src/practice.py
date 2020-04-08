# for i in range(10):
#     print(i)

# a = [1,2,3,4]

# for i in a: #Iterable
#     print(i)

# a = (1,2,3)

# for i in a: #Iterable
#     print(i)

# f = open("foo.txt")

# for i in f:
#     print(i)

#################################################################################

class Animal: #represents the blueprint
#     def __init__(self): #CONSTRUCTOR function that gets called when the animal is contructed from this blueprint, first Arugement is ALWAYS "SELF"
#         print("contructor called!")
#         self.leg_count = 4


# cat = Animal()  #contrust a new Animal, the "cat" is a OBJECT, ANIMAL is the class, Instantiate a new Animal
# dog = Animal()  #"cat and dog" is an instance of a animal or they are a animal




# print(f"cats leg count: {cat.leg_count}")

# cat.leg_count = 3

# print(f"cats leg count: {cat.leg_count}")
# print(f"dog leg count: {dog.leg_count}")

# rabbits = [
#     Animal(),
#     Animal(),
#     Animal()
# ]

# rabbits[1].leg_count = 3  #leg_count is an "ATTRIBUTE" on the object
# print(f"rabbit 0's leg count: {rabbits[0].leg_count}")
# print(f"rabbit 1's leg count: {rabbits[1].leg_count}")
# print(f"rabbit 2's leg count: {rabbits[2].leg_count}")

######################################################################

class Animal: 
    def __init__(self, leg_count=4): 
        
        self.leg_count = 4
        self.likes_food = True

    def get_leg_count(self): #getter
        return self.leg_count

    def set_leg_count(self, leg_count): #setter
        self.leg_count

cat = Animal()  #contrust a new Animal, the "cat" is a OBJECT, ANIMAL is the class, Instantiate a new Animal
dog = Animal()  #"cat and dog" is an instance of a animal or they are a animal
centipede = Animal(100)

l = cat.get_leg_count
print(l)

cat.set_leg_count(3)
l = cat.get_leg_count()
print(l)

######################################################################
"""A store can have multiple departments. A department can hold multiple products. The store
has a name. Departments have names. Products have names and prices.

Nouns tend to be classes.
If a noun "has" something, that something tends to be an attribute.
Verbs tend to be methods
"""

class Store: #Holds information about a store
    def __init(self, name, departments=None): #Construct a new store
        self.name = name
        
        if departments is None:
            self.departments = []
        else:
            self.departments = departments

class Department:
    def __init(self, name):
        self.name = name

    def add_product(self, product):
        self.products.append(products)

class Product:
    def __init(self, name):
        self.name = name
        self.price = price

soccer_ball = Product("soccer ball", 42.99)
sporting_goods = Department("Sporting Goods")
sporting_goods.add_product(soccer_ball)