#Custom Line#

response = input("What line do you want to add to the text? ")

file = open("random.txt", "a")
file.write(response)
file.close()

file = open("random.txt", "r")
print(file.read())