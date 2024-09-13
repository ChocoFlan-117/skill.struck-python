#Subtracting in a 2D List#

cols = [2, 5, 10, 100]

rows = [int(n) for n in input("Input a list of numbers: ").split()]

result = [] #Stores all the lists

for i in rows:
    col = [] #Creates a new list for each row
    for j in cols:
        col.append(i - j) #Compute and append each element
    result.append(col) #Add the computed list to the result
print(result)