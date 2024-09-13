#Weekend#

class Friday:
    def __init__(self, activity, friend):
        self.activity = activity
        self.friend = friend
    def pictures(self):
        print("We took so many pictures!")

thisWeekend = Friday("Movie", "Charlotte")

thisWeekend.friend = "Shane"

thisWeekend.money = 20

print(thisWeekend)

print(thisWeekend.money)

print(thisWeekend.friend)