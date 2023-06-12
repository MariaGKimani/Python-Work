import math
import statistics
# Write a function that takes a list of numbers as input and returns the sum of all the numbers in the list.
def lstnum (numbers):
    xx = 0
    for num in numbers:
        xx += num
    return xx
print(lstnum([2,3,4,6,7,8,9]))  

# Write a function that takes a string as input and returns the string reversed.
def reverseeed(str):
    rvse = str[::-1]
    return rvse
print(reverseeed('Maria'))

def revers(lst):
    rvsep = lst[::-1]
    return rvsep
print(revers([4,3,5,6,7,8]))

# Write a function that takes two numbers as input and returns 
# the greatest common divisor (GCD) of the two numbers.
def finds_gcd(num1,num2):
    while num2 !=0:
        num1,num2=num2,num1%num2
        return num1
    
print(finds_gcd(16,8))


def ccc(num1,num2):
     x= math.gcd(num1,num2)
     return x
print(ccc(16,8))

y = math.pow(2,3)
print(y)

# Write a function that takes a list of integers as input
#  and returns a new list with only the even numbers from the original list.
def lstnnn(lsst):
    new_Arr =[]
    [new_Arr.append(l)for l in lsst if l %2 == 0]
    return new_Arr
print(lstnnn([2,3,4,5,7,8,9,4,2]))

def x (listss):
    newX = []
    for i in listss:
        if i %2 ==0:
            newX.append(i)
    return newX
print(x([9,8,6,4,2,3]))

# Write a function that takes a list of strings as input 
# and returns a new list with only the strings that have a length greater than 5.
def string_greater5(str_list):
    new_arr = []
    [new_arr.append(string) for string in str_list if len(string) > 5]
    return new_arr
print(string_greater5(['Mother', 'Veronicaaaa', 'Vee', '12345678', 'Anita']))
def use_for(list_str):
    new_arr = []
    for string in list_str:
        if len(string) > 5:
         new_arr.append(string)
    return new_arr
print(use_for(['Mother', 'Veronicaaaa', 'Vee', '12345678', 'Anita']))

# Write a function that takes a string as input and returns True
#  if the string is a palindrome, and False otherwise.
def palindrome(sttrrr):
    if sttrrr[::-1] ==sttrrr:
        return True
    else:
        return False
    
print(palindrome("Mariagoretti"))
print(palindrome("wow"))

# Write a function that takes a list of numbers as input and
# returns the median value of the numbers in the list.
def list_number(list):
    x = statistics.median(list)
    return x
print(list_number([1,2,3,4,5,6,7,8,9,10,11]))

# Write a function that takes a list of integers as
# input and returns the product of all the numbers in the list.
def list_integers(listInt):
    product =1
    for num in listInt:
        product *= num
    return product
print(list_integers([3,2,2,4]))

# Write a function that takes a string as input 
# and returns a new string with all the vowels removed.
def  vowels(stttt):
    vowels = "aeiouAEIOU"
    empt_str=""
    for char in stttt:
        if char not in vowels:
            empt_str +=char
    return empt_str

print(vowels("eggeeillio"))



# Write a function that takes a list of integers as 
# input and returns a new list with only the unique 
# elements from the original list.
def remove_dups (list_ints):
    newL =[]
    for i in list_ints:
        if i  not in newL:
            newL.append(i)
    return newL
print(remove_dups([1,1,2,3,3,5,5,6,6,7,8,8]))


def xx(*str):
    x =[]
    [x.append(s.upper())for s in str]
    # for s in str:
    #     x.append(s.upper())
    return x
print(xx("maria","serah","esther"))

# Write a function that takes a list of numbers 
# as input and returns the average (mean) value of the numbers in the list.
def list_num (lst):
    x = statistics.mean(lst)
    return x
print(list_num([1,2,3,4,5,6,8]))

# Write a function that takes a string as input and
# returns a new string with all the words in reverse order
def  stringss(str):
    x = str[::-1]
    return x
print(stringss("maria"))
# Write a function that takes a list of integers as input
# and returns the smallest positive integer that is not in the list.




# Write a function that takes a list of numbers as input
# and returns a new list with the numbers 
# sorted in descending order
def lst_number(lssst):
    x = sorted(lssst, reverse=True)
    return x
print(lst_number([1,4,5,6,0,2,3]))

def xx (xxx):
    y = sorted(xxx)
    print(y)
xx([25,34,67,16])
# Write a function that takes a string as input and returns 
# True if the string contains only digits, and False otherwise.




def xx(*para):
    get_list = list(para)
    return get_list
print(xx(1,2,3,4,5,6,7,6,6,4,3,3,"hello"))


import math
def factorials(num):
    num2 = math.factorial(num)
    return num2
print(factorials(3))



        

