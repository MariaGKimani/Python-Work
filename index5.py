# Given a list of numbers, use list comprehension to
# remove all odd numbers from the list:
# numbers = [3,5,45,97,32,22,10,19,39,43]

def lstc (numbers):
    return[num for num in numbers if num % 2 !=0]
numbers = [3,5,45,97,32,22,10,19,39,43]
print(lstc(numbers))


# Find the common numbers in two lists
# (without using a tuple or set)
list_a = 1, 2, 3, 4,
list_b = 2, 3, 4, 5

common =[]

for num1 in list_a:
    if num1 in list_b:
        common.append(num1)
print(common)


# Use a nested list comprehension to find all of the numbers
# from 1-1000 that are divisible by any single digit besides 1 (2-9)


# Write a Python function to remove
#  all vowels in a string
def rmvowels(ssttrr):
    string = ''
    vowels = 'aeiou'
    for str in ssttrr:
        if str.casefold() not in vowels:
            string += str
    return string
print(rmvowels("Maria"))


# Write a Python program that takes a list of strings 
# as input and outputs the number of times each string 
# appears in the list, using a dictionary and conditional statements.



# Write a Python program that takes a list of numbers 
# as input and outputs the median of the numbers
import statistics
def lstio(numss):
   x =  statistics.median(numss)
   return x
print(lstio())