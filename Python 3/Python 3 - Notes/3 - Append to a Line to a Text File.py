#Notes:



##########
#OVERVIEW#
##########
#There are two ways to edit files with Python: 
#1. Append text to the file.
#2. Overwrite the contents of the file completely. 

#You specify what you're doing with the file when you use the open() function.

file = open("example.txt", "r")
#^ The "r" in this code is to read the file.

#(Add)
#If you use the "a" command, you open the file in "append" mode which adds all new text to the end of what's already there.

#(Replace)
#If you use the "w" command, you open the file in "write" mode which completely deletes the old text and replaces it with your new text.



#############
#APPEND MODE#
#############
file = open("example.txt", "a")
#^ Append mode (Adding new text)
file.write("This is the new line added!")
#^ You can add a new line by using the write() command
file.close()

#To be able to see if it worked:
file = open("example.txt", "a")
file.write("This is the new line added!")
file.close()

file = open("example.txt", "r")
print(file.read())