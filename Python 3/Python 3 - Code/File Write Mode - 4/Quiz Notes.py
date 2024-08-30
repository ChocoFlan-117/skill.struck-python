##############
#What does the following code do if a file called "report.txt" doesn't already exist?
file = open("report.txt", "w")
#Answer: It will create a new text file named report.txt
#############



#############
#What will the following code do to the text file named practice?
file = open("practice.txt", "a")
file.write("Good morning!")
file.close()
#Answer: It will append the line "Good morning!" to the file named practice.txt
#############



#############
#What will the following code do to the text file named practice?
file = open("practice.txt", "w")
file.write("Hey you!")
file.close()
#Answer: It will replace everything in the file named practice.txt with "Hey you!"
##############



##############
#True or false: After you use Python code to create a new text file, you can write to, append, and read that text file like any other text file.
#Answer: True
#############



##############
#What does the w stand for in the following code?
file = open("example.txt", "w")
#Answer: write
###############



##############
#True or False: The write mode replaces everything that was in the text file.
#Answer: True
##############



#############
#What will the following code do if there is no file named tractor?
file = open("tractor.txt", "w")
#Answer: It will create a file named tractor
#############