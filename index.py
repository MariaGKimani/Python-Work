#Write a Python function that takes a list of integers
#as input and returns the sum of all the even numbers in the list.
def list_integers(*lists):
        count =0
        for a in lists:
               if  a %2 == 0:
                    count += a
                    
        print(count)
list_integers(1,2,4,6,8,9,90)

#Write a Python function that takes a string as input and returns
#a list of all the words in the string that have more than three letters.
def fun_strings(strings):
    fun_string = strings.split()
    xx = [fun for fun in fun_string if len(fun) > 3]
    return xx
      
print(fun_strings("Maria loves Kotlin Javascript and Python"))

##Write a Python program that takes a list of numbers 
# #as input and adds all odd numbers.
def list_num (listss):
        const_new = 0
        for x in listss:
            if x % 2 != 0:
                  const_new += x
        return(const_new)
print(list_num([1,3,5,7,9,0,4,3,7]))


#Write a Python program that takes a list of numbers 
# as input and sorts the list in descending order.
def descend_list(*lessst):
    print(sorted(lessst).reverse()) 
descend_list(10,20,40,2,4,6,37,33,15,18)



# Write a Python function that takes two lists as input and 
# returns a new list that contains all the 
# elements that are common to both lists.
# def two_list(*list1,list2):
#       newX = list1.intersection(list2)
#       print(newX)
# two_list((1,2,3,4,5,6),(87,4,5,34,66,55))     

#Write a Python program that takes a string as input
# and checks whether the string is a palindrome (
# i.e., reads the same backward as forward)
# def input_pal(s):
#        if x(s) ==x(s)[::-1]:
#         return("Palindrome")
#        else:
#             return("not palindrome")
# print(input_pal)