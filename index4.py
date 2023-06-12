# Write a Python function that takes two arguments 
# (a and b) and returns their sum.
def  argsss(num1,num2):
    return num1 +num2
print(argsss(24,30))
# Write a Python function that takes a string 
# as input and returns the string reversed.
def strr(strng):
    return strng[::-1]
print(strr("maria"))

# def strr(strng):
#     x = sorted(strng,reverse=True)
#     return x
# print(strr("maria"))

# Write a Python function that takes a 
# list of integers as input and 
# returns the sum of all the integers in the list.
def lst(ints):
    return sum(ints)
print(lst([1,2,3,4,5,5]))

# or or or or or
def lst3(ints2):
    num3 = 0
    for i in ints2:
        num3 +=i
    return num3
print(lst3([1,2,3,4,5,5]))

# Write a Python function that takes a list of integers as
# input and returns a new list with all the even numbers removed
def lst2(lstint):
    return [x for x in lstint if x%2 != 0]

print(lst2([1,2,3,4,5,6,8,6,4,3]))



# Write a Python function that takes
#  a list of integers as input 
# and returns the highest value in the list
def  lst4(lstint2):
    return max(lstint2)
print(lst4([1,2,3,4,5,6,7,89]))

# Write a Python function that takes a list of strings
# as input and returns a new list with 
# all the strings capitalized.

def lst5(lstint3):
    return [xxx.capitalize() for xxx in lstint3]
   
print(lst5(["maria","goretti","kimani"]))

# Write a Python program to get a single string
# from two given strings, separated by a space,
# and swap the first two characters of each string





# Write a Python function that takes a list of words
# and returns the longest word and the length of
# the longest one
def wordword(words):
    longestword =''
    longestlength =0
    for word in words:
        if len(word) > longestlength:
            longestword = word
            longestlength = len(word)
    return longestlength,longestword
print(wordword(["maria","goretti","kimani"]))


# Write a Python program that accepts 
# a comma-separated sequence of words as
# input and prints the distinct words in 
# sorted form (alphanumerically).

# def comma(words2):



# Write a Python function that takes two lists 
# and returns True if they have at least one
# common member.

def xx(lst66,list77):
    for item in list77:
        if item in lst66:
            return True
    return False
print(xx([1, 2, 3, 4, 5],[6, 7, 8, 9, 10]))


#  Write a Python program to convert a list 
# to a list of dictionaries.
# Sample lists: 
# ["Black", "Red", "Maroon", "Yellow"],
# ["#000000", "#FF0000", "#800000", "#FFFF00"]



# Write a Python program to check 
# whether all dictionaries in a
#  list are empty or not

