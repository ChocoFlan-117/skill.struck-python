#Notes:

#Using write mode is almost the exact same as using append mode. 
#The main difference is that write mode replaces everything that was in the text file.

#Write mode is done by including the w command in the open() function.
file = open("example.txt", "w")
file.write("This line replaces everything in this file!")
file.close()
#This line replaces everything in this file!



#####################
#CREATING A NEW FILE#
#####################
#Both the "write" and "append" modes can also be used to create a brand new text file.
#If there is no text file with that name it will create a new one.

#This code below would create a brand new document, since a file called "new_document.txt" does not currently exist:
file = open("new_document.txt", "w")
#Then you can write to, append, read, and close this file just like any other text file.