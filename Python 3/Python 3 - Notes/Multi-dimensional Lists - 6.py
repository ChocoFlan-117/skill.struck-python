#Notes:
#Multi-dimensional lists are lists with more than one dimension. 



##########
#OVERVIEW#
##########
#A list looks like this:
list = [1, 1, 1, 1, 1]

#A 2 dimensional list:
list = [[1, 1, 1, 1, 1], [2, 2, 2, 2, 2], [3, 3, 3, 3, 3], [4, 4, 4, 4, 4]]


#3D, 4D, or lists with any number of dimensions are possible.



############################
#HOW FOR LOOPS CREATE LISTS#
############################
#One-dimensional list:
n = 5
list = []
for i in range(n):
    list.append(0)
print(list)
#[0, 0, 0, 0, 0]
#^ This code uses a for loop and creates a list of 5 elements, and puts the value "0" in each element.

#With a 2D list it's helpful to view it as having rows and columns. 
#A 1D list only has columns, when we add a second dimension we are adding in additional rows. 
#The code to create this:
rows = [1, 2, 3]
cols = ["red", "orange", "yellow", "green"]
list = []
for i in rows:
    col = []
    for j in cols:
        col.append(j)
    list.append(col)
print(list)
#[['red', 'orange', 'yellow', 'green'], ['red', 'orange', 'yellow', 'green'], ['red', 'orange', 'yellow', 'green']]



#################################
#USING RANGE TO CREATE 2D LISTS#
#################################
rows = 5
cols = 5
list = []
for i in range(cols):
    col = []
    for j in range(rows):
        col.append(i)
    list.append(col)
print(list)
#[[0, 0, 0, 0, 0], [1, 1, 1, 1, 1], [2, 2, 2, 2, 2], [3, 3, 3, 3, 3], [4, 4, 4, 4, 4]]
#^ This code uses one for loop to create the columns, and another for loop to create the rows in those columns. 
#This is called nested for loops.