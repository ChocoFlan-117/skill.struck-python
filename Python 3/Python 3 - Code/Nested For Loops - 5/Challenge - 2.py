#Weather Watcher#

rows = input("List of weather: ").split()

cols = ["windy", "breezy", "calm"]

result = [[weather + " " + wind for wind in cols] for weather in rows]

print(result)