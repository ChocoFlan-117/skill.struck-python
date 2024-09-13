#Vacation Planner#

class Vacation:
    def __init__(self, location, activity, food):
        self.location = location
        self.activity = activity
        self.food = food

one = Vacation("one", "two", "three")
two = Vacation("one", "two", "three")
three = Vacation("one", "two", "three")

print("Print this, " + one.location)
print("then this, " + two.activity)
print("and this, " + three.food)