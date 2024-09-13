################
#Which method of programming is faster for the computer to calculate?
#Answer: recursion
################



################
#True or False: There are usually many ways to get to the same answer in programming. Some are faster or more efficient for the computer to calculate than others.
#Answer: True
################



################
#What approach is the following code an example of?
def answer(n):
  if n <= 1:
    return 1
  else:
    return n + (answer(n - 1))
    
print(answer(10))
#Answer: Recursion
################