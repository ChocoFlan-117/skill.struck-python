#Notes:
#Stacks are one of the fundamental data structures used in computer science.



##########
#OVERVIEW#
##########
#A stack is a data storage technique. 
#Characterized by a last in, first out strategy.
#When you add data to a stack, the most recent addition is the first thing that is returned. 
#Stacks have two main funtions: "append()"/"push()" and "pop()"

#"push()" and "append() do the same thing.

#Example of a stack:
stack = [1, 2, 3, 4, 5]

#Stacks look a lot like lists because lists are a kind of stack.
#Think of the list as tipping counter clockwise on its end. The end of the list then becomes the top of the stack.



##########
#APPEND()#
##########
#Lists can be used as stacks.

#The "append()" function is how data is added to a stack. The "append()" function can be thought as "placing it" onto the top of the stack.



#######
#POP()#
#######
#Pop is the opposit of "push()". The "pop()" function deletes the very top element of the stack. 

#Example:
stack = []

stack.append('a')
stack.append('b')
stack.append('c')

stack.pop()

print(stack)
#['a', 'b']

#We appended (or "pushed") three charcaters onto the stack.
#When the "pop()" function is used it deletes the most recently added character. 