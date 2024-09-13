this_list = ['panda', 'lion', 'giraffe', 'tiger', 'elephant', 'monkey', 'fish', 'snake', 'bearded dragon', 'koala']

def feeding(this_list):
    if len(this_list) == 1:
        print("The " + this_list[0] + " has been fed")
    else:
        mid = len(this_list)//2
        first_half = this_list[:mid]
        second_half = this_list[mid:]
        feeding(first_half)
        feeding(second_half)


feeding(this_list)