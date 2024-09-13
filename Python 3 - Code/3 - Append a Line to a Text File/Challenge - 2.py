#Give Credit#

file = open("random.txt", "a")
file.write("Quote was said by Gandhi")
file.close()

file = open("random.txt", "r")
print(file.read())