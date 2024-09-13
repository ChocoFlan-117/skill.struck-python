#Notes:

#Basic class with some objects created using the constructor:
class Dog:
    def __init__(self, name, age, gender):
        self.name = name 
        self.age = age
        self.gender = gender

pet = Dog("Jasmine", "15", "Female")

print(pet)



####################################
#ADDING AN ATTRIBUTE TO THE OBJECT#
####################################
class Dog:
    def __init__(self, name, age, gender):
        self.name = name
        self.age = age
        self.gender = gender

pet = Dog("Jasmine", "15", "Female")

pet.height = 12

print(pet.height)
#12



######################################
#REMOVING AN ATTRIBUTE TO THE OBJECT#
######################################
#We can also remove an attribute to the object by using delattr()

class Dog:
    def __init__(self, name, age, gender):
        self.name = name
        self.age = age 
        self.gender = gender

pet = Dog("Jasmine", "15", "Female")

delattr(name)

print(pet.name)
#NameError: name 'name' is not defined



##########################
#MODIFY OBJECT PROPERTIES#
##########################
#We can also change the values in our objects.

class Dog:
    def __init__(self, name, age, gender):
        self.name = name
        self.age = age
        self.gender = gender

pet = Dog("Jasmine", "15", "Female")

print(pet.name)

pet.name = "Franz"

print(pet.name)
#Jasmine
#Franz



##########################
#DELETE OBJECT PROPERTIES#
##########################
#We can also remove the values in our objects.
#This is done use the "del" keyword.

class Dog:
    def __init__(self, name, age, gender):
        self.name = name
        self.age = age 
        self.gender = gender

pet = Dog("Jasmine", "15", "Female")

print(pet.name)

del pet.name

print(pet.name)
#Jasmine
#AttributeError: 'Dog' object has no attribute 'name'

#This will throw an error because there is no longer a value for "pet.name"



################
#OBJECT METHODS#
################
#We can also add functions to our classes. These functions are called methods.

#Adding a function named "greeting" and put it in the class named "Person", this function will print out "Good Morning".

class Dog:
    def __init__(self, name, age, gender):
        self.name = name
        self.age = age
        self.gender = gender

    def greeting(self):
        print("Good Morning")

pet = Dog("Jasmine", "15", "Female")

pet.greeting()
#Good Morning

#Notice how we passed the parameter self into the finction declaration? 
#This is so that the function is used in this partcular instance of this class.