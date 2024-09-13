#Shopping#

class Shopping:
    def __init__(self, item, quality):
        self.item = item
        self.quality = quality
        self.total = []
        
    def spending(self, cost):
        self.total.append(cost)

sportStore = Shopping("Kayak", "High Quality")

sportStore.spending(12)
sportStore.spending(23)
sportStore.spending(31)

print(sportStore.total)