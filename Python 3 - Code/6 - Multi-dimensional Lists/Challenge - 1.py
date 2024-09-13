#Secret Agent Name Generator#

first_names = ["name1", "name2", "name3", "name4"]
last_names = ["name1", "name2", "name3", "name4"]

name = []

for i in (first_names):
    name2 = []
    for j in (last_names):
        name2.append(j + " " + i)
    name.append(name2)
print(name)