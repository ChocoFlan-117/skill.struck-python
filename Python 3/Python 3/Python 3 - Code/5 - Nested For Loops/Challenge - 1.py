#Multiply by the Number of Rows#

mylist = [1, 2, 3, 4, 5]

rows = int(input("How many rows do you want? "))


newlist = [[(j*rows) for j in mylist] for i in range(rows)]
#^ Outer loop: (for i in range(rows))
#   Runs the input amount of times (for now 3, so it runs 3 times)

#Inner loop: [(j*rows) for j in mylist]
#   For each row, it calculates each element in "mylist" multipled by "rows" (3)

print(newlist)