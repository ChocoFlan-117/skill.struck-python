#Notes: 
#The read() function also allows us to only read parts of the file. By default this function reads the entire file, but if we add a number it will read that many characters from the file.

#Let's say our "example.txt" file has the alphabet text inside it
#abcdefghijklmnopqrstuvwxyz.

#This code would print the entire alphabet:
file = open("example.txt", "r")
print(file.read())

#While this code would only print out the first 5 characters:
file = open("example.txt", "r")
print(file.read(5))

#The number 5 is telling the code to print five characters. This is not using indexing, which starts counting at 0. (So it starts at 1)



########################
#READ LINES OF THE FILE#
########################
#The readline() function will read entire lines of the text file. 

#Let's say this is our example text file:
#Hello! This is a test file!
#I hope you're enjoying learning how to code!
#Lolz :3

file = open("example.txt", "r")
print(file.readline())
#^ This code will open the text file named example.txt then it reads the first line of that text file.
#Hello! This is a test file!

#Calling readline() twice will read the first two lines of the file:
file = open("example.txt", "r")
print(file.readline())
print(file.readline())
#^ This will print out:
#Hello! This is a test file!
#I hope you're enjoying learning how to code!



####################################################
#READ LINES OF THE FILE - READLINE() & READLINES()#
####################################################
#To return all the lines in a file as a list with each list item being a line, use the following code. (This code uses readlines instead of readline.)

file = open("example.txt", "r")
priint(file.readlines())



###############
#CLOSING FILES#
###############
#When your program is finished reading the file, it's important to close it. This is done in your Python file by calling the close() function on your variable named file.
file.close()