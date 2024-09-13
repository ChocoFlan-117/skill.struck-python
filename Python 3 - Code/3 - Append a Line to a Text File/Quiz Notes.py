###########
#What would we place in the empty quotation marks to read the text file?
file = open("Aimee.txt", " ")
#Answer: r
###########



#############
#What would we place in the empty quotation marks to append a line to the text file?
file = open("example.txt", " ")
#Answer: a 
############



############
#Where will the new line appear in the text file when this code is run?
file = open("example.txt", "a")
file.write("This is the new line we added!")
file.close()
#Answer: At the end of the text file
##############



##############
#What happens if you use a w in the empty quotation marks of this code?
#Answer: It will completely delete the old text in the text file and replace it with your new text
############



#############
#What does the a stand for in the following code?
file = open("example.txt", "a")
#Answer: append
############



###########
#What will the following code do?
file = open("example.txt", "a")
file.write("Sincerely, Inej")
file.close()
#Answer: It will add the line "Sincerely, Inej" to the end of the file named example
###########