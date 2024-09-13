#Books and Sequels#

books = [int(n) for n in input("Input a list of numbers").split()]

def pair(books):
    if len(books) == 2:
        result = books[0] + books[1]
        print(result)
    else:
        mid = len(books)//2
        pair(books[:mid])
        pair(books[mid:])

if len(books) % 2 != 0:
    print("Please enter an even number of data points.")
else:
    pair(books)