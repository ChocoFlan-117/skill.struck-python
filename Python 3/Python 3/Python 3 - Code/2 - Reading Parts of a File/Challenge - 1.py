#Read a Specific Number of Characters#

integer = int(input("Choose a number: "))

file = open("cobra.txt", "r")
print(file.read(integer))

file.close()