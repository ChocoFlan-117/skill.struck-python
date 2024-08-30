#Notes:

#Nested for loops are when you use a for loop inside of another for loop.

#To creat a 1D list:
n = 5
list = []
for i in range(n):
    list.append(i)
print(list)
#[0, 1, 2, 3, 4]

#To create a 2D list:
rows = 5
cols = 5
list = []
for i in range(cols):
    col = []
    for j in range(rows):
        col.append(j)
    list.append(col)
print(list)
#[[0, 1, 2, 3, 4], [0, 1, 2, 3, 4], [0, 1, 2, 3, 4], [0, 1, 2, 3, 4], [0, 1, 2, 3, 4]]

#Explaination of code:
#We have two lists—one named rows and one named cols.

#We also have an empty list named list.

#The code for i in rows: says that we are going to go through the variable named rows, one at a time. So we start with the 1.

#Inside the first for loop we have an empty list named col = [ ]. And then inside the first for loop we have another loop. 
#This is called a nested for loop. (It means for each item in the list named rows, we will do another loop.)

#So remember that we are still working on our first loop for the 1 in the list named rows. For just that 1, we are looping through all five values in the list named cols. What are we doing when we loop through the list named cols? We are appending a value of j. The value of j is whichever value in the list named cols that we are currently on.

#That sounds complex, but for that first value in the list named rows, we end up with another list:

#["red", "orange", "yellow", "green"']

#This list then gets appended to the empty list named list.

#Then we do the whole loop again starting with the value of 2 in the list named rows. So by the end we end up with three rows of values.

#["red", "orange", "yellow", "green"']

#["red", "orange", "yellow", "green"']

#["red", "orange", "yellow", "green"']

#On your screen, each of these lists is in a bigger list. So it looks like this:

#[ ["red", "orange", "yellow", "green"'], ["red", "orange", "yellow", "green"'], ["red", "orange", "yellow", "green"'] ]



####################
#ONE LINE FOR LOOPS#
####################
#Python has the ability to allow us to write a for loop that only takes up one line.

#Example:
list = ["hello" for i in range(5)]
print(list)
#['hello', 'hello', 'hello', 'hello', 'hello']

#This will create a list 5 indexes long, with "hello" as the value in all the indexes.


#One line nested for loops can also create multi-dimensional lists.

#Example: (creates a 2D list)
rows = 3 
my_list = [1, 2, 3, 4, 5]
list = [[j for j in my_list] for i in range(rows)]

print(list)
#[[1, 2, 3, 4, 5], [1, 2, 3, 4, 5], [1, 2, 3, 4, 5]]