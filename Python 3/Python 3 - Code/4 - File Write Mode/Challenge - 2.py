#Custom Greeting Cards#

answer = input("Greeting Card: ")

file = open("report.txt", "w")
file.write(answer)
file.close()

print(file.read())