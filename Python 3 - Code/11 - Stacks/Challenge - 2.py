#Foods with the Letter S#

answer = ["apples", "steak", "potatoes", "carrots"]

user = input("Add to the stack: ")


if "s" in user or "S" in user:
    answer.append(user)
    print(answer)
else:
    print("The input doesn't have the letter s")