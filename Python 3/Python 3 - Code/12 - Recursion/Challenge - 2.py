#Pollinating Bees#

flowers = [int(n) for n in input("How many blossoms are on each tree?").split()]

def orchard(flowers):
    if len(flowers) == 1:
        result = flowers[0] * 3
        print(result)
    else:
        mid = len(flowers) // 2
        orchard(flowers[:mid])
        orchard(flowers[mid:])

orchard(flowers)