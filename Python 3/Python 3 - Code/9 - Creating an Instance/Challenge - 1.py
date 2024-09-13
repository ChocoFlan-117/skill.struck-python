#A Fruit Festival#

class Fruit:
    def __init__(self, shape, kind, size):
        self.shape = shape
        self.kind = kind
        self.size = size

object1 = Fruit("shape1", "kind1", "size1")
object2 = Fruit("shape2", "kind2", "size2")
object3 = Fruit("shape3", "kind3", "size3")
object4 = Fruit("shape4", "kind4", "size4")

print(object1.kind)
print(object2.kind)
print(object3.kind)
print(object4.kind)