###########
#True or False: You must read an entire text file when using Python code.
#Answer: False
#########



#########
#Which piece of Python code would you use to read the first line of a text file?
#Answer: print(file.readline())
#########



############
#Which piece of Python code would you use to read the first 20 characters of a text file?
#Answer: print(file.read(20))
############



###########
#True or False: To print the first three lines from a text file, just use the following code 3 times in your Python file.
print(file.readline())
#Answer: True
#############



#############
#Which piece of code would you use to close the text file?
#Answer: file.close()
############



############
#How many lines of text will the following code print out?
file = open("example.txt", "r")
print(file.readline())
print(file.readline())
#Answer: 2
#############



##########
#What will the following code print out?
file = open("example.txt", "r")
print(file.read(5))
#Answer: The first 5 characters
###########