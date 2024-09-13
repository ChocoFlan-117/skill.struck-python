#How Many Words?#

file = open("cobra.txt", "r")

data = file.read()
    
words = data.split()

num_words = len(words)

print("Number of words in the file:", num_words)

file.close()