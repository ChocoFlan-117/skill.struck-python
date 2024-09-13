rows = 3
pets = ["str1", "str2", "str3", "str4", "str5"]



pets = [[pet for pet in pets] for _ in range(rows)]

print(pets)