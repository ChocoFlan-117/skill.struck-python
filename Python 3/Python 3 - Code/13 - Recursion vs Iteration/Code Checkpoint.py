user = int(input())

def factorial(user): 
	if user <= 1:
		return 1
	else:
		return (user * factorial(user - 1))

print(factorial(user))