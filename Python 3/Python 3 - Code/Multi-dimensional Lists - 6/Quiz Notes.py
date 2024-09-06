#############
#What kind of list is this an example of?
#Answer: One Dimensional List
##############



###########
#What kind of list is this an example of?
[[1, 2, 3], [1, 2, 3], [1, 2, 3]]
#Answer: Two Dimensional List
###########



#############
#True or False: A for loop can create a list.
#Answer: True 
###########



############
#What is the output of the code provided?
n = 5
list = []
for i in range(n):
    list.append(0)
print(list)
#Answer: [0, 0, 0, 0, 0]
############



#############
#What is the purpose of using the range function in the code for creating 2D lists?
rows = 5
cols = 5
list = []
for i in range(cols):
    col = []
    for j in range(rows):
        col.append(i)
    list.append(col)
print(list)
##answer: To determine the size of each row and column
############