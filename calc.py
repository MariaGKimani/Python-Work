#Remove all occurences of an item from a list
# Remove all occurrences of an item from a list
def y(lssst):
    item = 2
    my_list = [x for x in lssst if x != item]
    print(my_list)

y([1,2,2,3,4,2,5,6,6])


#checking if all items are unique
def unique(lst):
    if len (lst) == len(set(lst)):
        print("its a set","All items are unique")

unique([1,2,2,3,4,3,3,2,3,5,6,7,2,8,9])