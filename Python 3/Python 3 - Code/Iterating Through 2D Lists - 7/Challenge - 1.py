#Multiply List Values#

user = int(input("What would you like to multiply the list by? "))

my_list = [[0, 1, 2], [10, 15, 20], [100, 200, 300], [5, 6, 7]]

rows = 4
cols = 3

for i in range(rows):
    for j in range(cols):
        my_list[i][j] = my_list[i][j] * user

print(my_list)