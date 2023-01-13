# Question 1
# Write a function to print "hello_USERNAME!" USERNAME is the input of the function.
def hello_name(user_name):
    print("Hello, " + user_name.title() +"!")
hello_name("ashmika")


# Question 2
# Write a python function, first_odds that prints the odd numbers from 1-100 and returns nothing.
def first_odds():
    for odd_numbers in range(1,100):
       if odd_numbers % 2 != 0:
            print(odd_numbers)
first_odds()


# Question 3
# Please write a Python function, max_num_in_list to return the max number of a given list.
def max_num_in_list(a_list):
    maxi = a_list[0]
    for num in a_list:
        if num > maxi :
            maxi = num 
    return maxi
a_list=[50,33,10,12,99,0,14]
print("Max number = " + str(max_num_in_list(a_list)))


# Question 4
# Write a function to return if the given year is a leap year. 
# A leap year is divisible by 4, but not divisible by 100, unless it is also divisible by 400.
# The return should be boolean Type (true/false).
def is_leap_year(a_year):
    if (a_year % 4 == 0) and (a_year % 100 != 0):
        return True
    elif (a_year % 100 == 0) and (a_year % 400 == 0):
        return True
    else :
        return False
a_year = int(input("Enter any year in 'yyyy' format : "))
print ("Entered year is a leap year(True/False?) : " + str(is_leap_year(a_year)))


# Question 5
# Write a function to check to see if all numbers in list are consecutive numbers.
# For example, [2,3,4,5,6,7] are consecutive numbers, but [1,2,4,5] are not consecutive numbers. 
# The return should be boolean Type.
def is_consecutive(a_list):
    if sorted(a_list) == list(range(min(a_list), max(a_list)+1)):
        return True
    else:
        return False
a_list = [13,10,11,12,14,16,15]
print("The given list is consecutive (True/False?) : " + str(is_consecutive(a_list)))    


#END OF ASSIGNMENT