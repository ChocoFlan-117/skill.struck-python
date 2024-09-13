#########################
#What is the object in the following example?
class Dog:
	def __init__(self, name, age, gender):
		self.name = name
		self.age = age
		self.gender = gender
		
	def greeting(self):
		print("Good Morning")
	

pet = Dog("Jasmine", "15", "Female")

pet.greeting()
#Answer: pet
######################



#######################
#What will the following code print out?
class House:
   
	def __init__(self, build, size, location):
		self.build = build
		self.size = size
		self.location = location

myhouse = House("A frame", 2000, "Chicago")


myhouse.location = "Portland"

print(myhouse.build)
#A frame
#######################



#########################
#What will the following code print out?
class House:
   
	def __init__(self, build, size, location):
		self.build = build
		self.size = size
		self.location = location

myhouse = House("A frame", 2000, "Chicago")


myhouse.location = "Portland"

print(myhouse.location)
#Answer: Portland
########################



#####################
#What will the following code print out?
class House:
   
	def __init__(self, build, size, location):
		self.build = build
		self.size = size
		self.location = location

myhouse = House("A frame", 2000, "Chicago")

del House.size

print(myhouse.size)
#Answer: It will throw an error
######################



############################
#What is the object method in the following example?
class Dog:
	def __init__(self, name, age, gender):
		self.name = name
		self.age = age
		self.gender = gender
		
	def greeting(self):
		print("Good Morning")
	

pet = Dog("Jasmine", "15", "Female")

pet.greeting()
#Answer: greeting
#############################



#######################
#In the given code, what are "name," "age," and "gender" examples of?
class Dog:
   
   def __init__(self, name, age, gender):
         self.name = name
         self.age = age
         self.gender = gender

pet = Dog("Jasmine", "15", "Female")

print(pet)
#Answer: Attributes
########################



##########################
#What will be printed when the following code is executed?
class Dog:
   
   def __init__(self, name, age, gender):
         self.name = name
         self.age = age
         self.gender = gender

pet = Dog("Jasmine", "15", "Female")
print(pet.name)
#Answer: Jasmine
##########################



#######################
#How is a new attribute added to an object?
#Answer: Just by assigning a new attribute to a value.
###########################



###########################
#What does the following code snippet delattr(name) do in the following code?
class Dog:
   
   def __init__(self, name, age, gender):
         self.name = name
         self.age = age
         self.gender = gender

pet = Dog("Jasmine", "15", "Female")

delattr(name)

print(pet.name)
#Answer: Removes the 'name' attribute from the object
######################



######################
#True or False: Objects can also have their own methods.
#Answer: True
#######################