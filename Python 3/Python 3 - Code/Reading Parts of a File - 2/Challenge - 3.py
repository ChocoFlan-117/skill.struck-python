#How Many Lines?#

file = open("cobra.txt", "r")

lines = len(file.readlines())

print(lines)

file.close()