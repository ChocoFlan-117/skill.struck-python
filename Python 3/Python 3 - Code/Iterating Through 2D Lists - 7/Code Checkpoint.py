my_list = [[40, 45, 50], [6, 7, 8], [100, 200, 300], [50, 60, 70], [9, 0, 1]]

rows = 5 #Index starts at 0
cols = 3

for i in range(rows):
    for j in range(cols):
        my_list[i][j] = my_list[i][j] + 3

print(my_list)