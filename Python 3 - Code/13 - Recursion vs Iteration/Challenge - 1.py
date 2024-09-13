#Add the List#

list_of_nums = [int(n) for n in input().split()]

def add(list_of_nums):
    if len(list_of_nums) == 0:
        return 0
    else:
        return list_of_nums[0] + add(list_of_nums[1:])

print(add(list_of_nums))