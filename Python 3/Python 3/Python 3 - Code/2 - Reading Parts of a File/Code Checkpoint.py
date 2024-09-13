file = open(".txt", "r")

print(file.read(10))

print(file.readline())
print(file.readline())

file.close()