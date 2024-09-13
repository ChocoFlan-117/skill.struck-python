#Notes:



##########
#OVERVIEW#
##########
#Python programs have the ability to access other files on your computer. As long as you tell your program the exact location of the file, it can open it, read the contents, edit them, and make other changes.
#This can be useful in many different ways. Let's say you have been given a large folder with 10,000 text files, and been assigned to change all the names of the text files to 'file1.txt', file2.txt' and so on. You could do this one by one, which would likely take hours and hours to complete.
#With Python, you could write a short, simple program that can make all those changes in a matter of seconds!



#######################
#WHAT IS A TEXT FILE?#
#######################
#A text file is a file that has only information in it without any formatting. Often, when you type out an essay for a class, it has formatting such as margins, spacing, or indentation. A text file only has the information typed inside. 
#Text files are useful because they don't take up very much storage space. 
#Often, large databases of records are saved in text files to minimize the amount of storage they take. (Information such as financial records, medical information, or weather information are often saved as text files.)



###############
#READING FILES#
###############
#When writing a Python program to read a file, the first thing to do is open the file.

#First create a variable and assign it to the open() function. (This funtion takes in 2 parameters)
#1. The name of the file to open example.txt
#2. The mode in which to open it r

#Example:
file = open("example.txt", "r")
#^ This opens the file, and creates a file variable which is now called "file". We used the "r" mode in the function which stands for "read". (Because we opened it in this mode, it's not possible for us to change the file, our program can only read it.)

#To print the contents of the file, use the read() function in a print statement.
#Example:
file = open("example.txt", "r")
print(file.read())
#^ The read() function is called on the "file" variable and reads all the text in the file. It is then printed out with the print command.



###############
#CLOSING FILES#
###############
#When your program is finished reading the file, it's important to close it. This helps to free up working memory. This is done in your Python file by calling the close() function on your variable named file.

#Example:
file.close()

#So everything all together should look like this.
file = open("example.txt", "r")
print(file.read())
file.close()