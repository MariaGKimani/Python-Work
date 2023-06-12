# Write a function that takes a list of numbers as input
#  and returns a new list with all duplicate numbers removed.
def list_of_num(lists):
    return list(set(lists))
x= [1,2,3,3,4,5,5,6,6,7,8,8,9,9]
print(list_of_num(x))
