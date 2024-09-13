#Notes:



##########
#OVERVIEW#
##########
#Object Oriented Programming enables us to create more complex data structures that help us track information more easily. 
#While lists, strings, tuples, arrays, and dictionaries are helpful and useful, sometimes they aren't enough. This is where object-oriented programming comes into play.



#########
#CLASSES#
#########
#When object-oriented programming is in it creates objects called classes.
#A class is similar to a list or a dictionary, but we can customize it to track the exact information we want to use.


#In the example we're goin to create a "Person" class that allows us to track the "name", "age", and "gender" of a person.

#A class is a blueprint of an object.
#In our "Person" example, the class is the outline of the person and says that every person created using this class should have a "name", "age", and "gender". (This class specifies what specific information is needed about the person, but it doesn't actually create anything in our program.



##################
#CREATING A CLASS#
##################
#A class is a blueprint of an object. It's not actually the object itself, it's just the form we use to create the object.

#Just like a blureprint isn't actually a house, a class isn't actualy an object.

#To create a class called "Person", use the class keyword and "Person" is the name of the class. 
#That's always the first line of code in a class.
#Classes should be capitalized.

#Example:
class Person:

#Then, underneath that class declaration we put a function that is always the same. (No matter what type of class one is creating.)
#The function is init() which stands for initialize. (This function is used to intialize the class when we create our first object.)
def __init__()
#NOTICE:
#There are TWO underscores before the init and TWO underscores after the init in this code.
#There is also a space between the def and the first underscore. 
#It must be typed this way to work correctly. (This is correct Python syntax.)

#In the init() function we need to add parameters.
#Th init() function MUST always have a self parameter.
#We add in any attributes we want to our class to have. 

#In this example, the "Person" class will have "name", "age", and "gender" attributes, so these are added in as parameters.
#Example:
class Person:
    def __init__(self, name, age, gender)
    #The final step is to add in the attribute assignments>
    #This is where we set the name of the class attribute to the name of the person that's being created.
    #Example:
    self.name = name
    self.age = age
    self.gender = gender
#There always needs to be one of these assignments for each attribute of the class.

#REMEMBER:
#This class is not an object.
#This class is a template we use to create an object.
#(Another way to say creating an object using a class is to say we create an #instance# of the class.)



###########
#INSTANCES#
###########
#Instances are actual objects created using the class. Adding a person to our program using the class, the instance will be the actual person we created.

#For example, let's say we want to add our friend Jasmine. When we create Jasmine in our program, she will be an instance of the person class. 
#Her name attribute will be "Jasmine", her age will be "15" and her gender will be "female".