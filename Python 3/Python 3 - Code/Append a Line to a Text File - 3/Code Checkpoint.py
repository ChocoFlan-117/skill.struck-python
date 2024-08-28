file = open("random.txt", "a")
file.write("I love programming!")
file.close()

file = open("random.txt", "r")
print(file.read())