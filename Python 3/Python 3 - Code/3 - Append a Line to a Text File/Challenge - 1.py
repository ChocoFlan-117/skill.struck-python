#Pen Pal#

file = open("random.txt", "a")
file.write("From your Pen Pal")
file.close()

file = open("random.txt", "r")
print(file.read())