# iter1=[1,2,3,4,5,6,7,8,9,10]

# for i in iter1:
    # if i%3 == 0 and i%5 == 0:
    #     print("FizzBuzz")
    # elif i %3 ==0:
    #     print("Fizz")
    # elif i%5 == 0:
    #     print("Buzz")

for i in range(1,51):
    if i%3 == 0 and i%5 == 0:

        print("FizzBuzz",i)
    elif i %3 ==0:
        print("Fizz")
    elif i%5 == 0:
        print("Buzz")

# print((range(1,51)))


# Write a Python program that accepts
# a string and calculates the number of digits and letters.

# Sample Data : Python 3.2
# Expected Output :
# Letters 6
# Digits 2

# str1='qwertyuiojhgc'

# for i in range(len(str1))




# Write a Python program to convert a month name to a number of days.
# Expected Output:

# List of months: January, February, March, April, May, June, July, August
# , September, October, November, December                                
# Input the name of Month: February                                       
# No. of days: 28/29 days 

# input_str= input("enter month")
# day_30=['april','june','september','november']

# day_31=[]
# ex=input_str.lower()

# if ex in day_30:
#     print("30 days")
# elif ex =='feb':
#     print("28/29 days")


# Write a  Python program to check whether an alphabet is a vowel or consonant.
# Expected Output:

# aeiou - vowel

# Input a letter of the alphabet: k                                       
# k is a consonant.

# Write a Python program to get the next day of a given date.
# Expected Output:

# Input a year: 2016                                                      
# Input a month [1-12]: 08                                                
# Input a day [1-31]: 23                                                  
# The next date is [yyyy-mm-dd] 2016-8-24   


yr = int(input("enter year"))

if yr%400 ==0 or yr%4 == 0:
    year_flag=True
elif yr%100 == 0:
    year_flag=False
else:
    year_flag=False


print(year_flag)