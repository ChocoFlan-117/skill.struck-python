#Notes:

#Code that wll multiply each element of a 2D list by 2:
my_list = [[0, 1, 2], [10, 15, 20], [100, 200, 300], [5, 6, 7]]
rows = 4
cols = 3

for i in range(rows):
    for j in range(cols):
        my_list[i][j] = my_list[i][j] * 2

print(my_list)
#[[0, 2, 4], [20, 30, 40], [200, 400, 600], [10, 12, 14]]


#Code explanation:

#First, we have a 2D list named my_list. Now we are trying to access each item in each list that's inside the overall list named my_list. 
#We do this by using range( ).

#To know how many rows and how many columns the list has, we create variables for rows and cols.

#We create a for loop that moves through the range of rows. For each item, we also loop through a range of columns. 
#Then, we use the code t in this case, we are multiplying it by 2. (It's basically looking for the index of the overarching list AND the index of the nested list together.) You can just think of it this whole code my_list[i][j] as representing each item in the list in turn.


my_list = [["dog", "cat", "frog"], ["shark", "squid", "whale"], ["deer", "fox", "badger"]]
rows = 3
cols = 3

for i in range(rows):
    for j in range(cols):
        my_list[i][j] = my_list[i][j] + " is awsome"

print(my_list)
#[['dog is awesome', 'cat is awesome', 'frog is awesome'], ['shark is awesome', 'squid is awesome', whale is awesome'], ['deer is awesome', 'fox is awesome', 'badger is awesome']]

#Notice how the number rows needed to be updated to match the number of rows in the list named my_list