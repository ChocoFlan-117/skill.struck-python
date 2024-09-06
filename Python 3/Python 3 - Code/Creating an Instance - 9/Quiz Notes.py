################
#What is the following code an example of?
first = Animal("Furry", "Brown", "4 legs")
#Answer: An object
###################



###################
#What is another way of saying "create an instance of a class?"
#Answer: Create an object
##################



####################
#Which of the following is most similar to a blueprint?
#Answer: class
##################



###############
#Which of the following is the way to access the attribute "salad" in the object named myObject?
class Dinner:
   
   def __init__(self, main, side, drink):
         self.main = main
         self.side = side
         self.drink = drink

myObject = Dinner("pasta", "salad", "juice")

print(myObject)
#Answer: myObject.side
#####################



###################
#How many objects can be made with one class?
#Answer: As many as you want
##################



###################
#Which term is used to describe an actual object created from a class blueprint?
#Answer: Instance
###################



###################
#How do you access the attributes of an object named p1?
#Answer: p1.attribute
######################



###################
#What does the following code print?
class Person:
   
   def __init__(self, name, age, gender):
         self.name = name
         self.age = age
         self.gender = gender

p1 = Person("George", "67", "Male")

print("Person 1: " + p1.name + " " + p1.age + " " + p1.gender)
#Answer: Person 1: George 67 Male
##################



###################
#What is the purpose of creating multiple instances of a class?
#Answer: To customize attributes for each instance
###################