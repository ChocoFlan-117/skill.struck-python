#Fruit Blender#

flavors = ["apple", "grape", "peach", "cinnamon", "vanilla"]

user = input("Input a list of fruits: ").split()

flavor_comb = []

for fruit in (user):
    flavor2 = []
    for flavor in (flavors):
        flavor2.append(fruit + " " + flavor)
    flavor_comb.append(flavor2)
print(flavor_comb)