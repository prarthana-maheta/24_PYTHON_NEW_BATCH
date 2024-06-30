# Prompt the user to input a year and convert it to an integer, assigning it to the variable 'year'
year = int(input("Input a year: "))

# Determine if the input year is a leap year

# Check if the year is divisible by 400
if (year % 400 == 0):
    leap_year = True
# Check if the year is divisible by 100
elif (year % 100 == 0):
    leap_year = False
# Check if the year is divisible by 4
elif (year % 4 == 0):
    leap_year = True
else:
    leap_year = False

# Prompt the user to input a month in the range of 1-12 and convert it to an integer, assigning it to the variable 'month'
month = int(input("Input a month [1-12]: "))

# Determine the number of days in the specified month

# Check for months with 31 days
if month in (1, 3, 5, 7, 8, 10, 12):
    month_length = 31
# Check for February
elif month == 2:
    # Check for leap year and assign the appropriate number of days
    if leap_year:
        month_length = 29
    else:
        month_length = 28
# For months with 30 days
else:
    month_length = 30

# Prompt the user to input a day in the range of 1-31 and convert it to an integer, assigning it to the variable 'day'
day = int(input("Input a day [1-31]: "))

# Calculate the next date based on the provided day, month, and year

# Check if the day is less than the total number of days in the month
if day < month_length:
    day += 1
else:
    day = 1
    # Check if the current month is December
    if month == 12:
        month = 1
        year += 1
    else:
        month += 1

# Display the next date in the format [yyyy-mm-dd] based on the updated day, month, and year
print("The next date is [yyyy-mm-dd] %d-%d-%d." % (year, month, day))



# Write a  Python program to construct the following pattern, using a nested loop number.

# 1
# 22
# 333
# 4444
# 55555
# 666666
# 7777777
# 88888888
# 999999999

# for i in range(1,10):
#     print(str(i)*i)


# break 
# continue 
# pass 

# i=1
# while i > 0:
#     pass
#     print("Yes") 
    # # break
    # continue
    # print("NO")
    # pass

# # write a python program to print the square of all the number for given range using while loop


# # print(f" Square of : {i} is ")
# # i=1
# # n=5
# # while i<=5:
# #     print(i*i)
# #     i+=1
# #     if i == n+1:
# #         break

# # list string tuple

# # t1 = (1,2,3) --immutable
# "I also love JAVA"

# # "Python happy to study"

# # tuple1=("Python","happy","To","Study")

# # Write a Python program to replace the last value of tuples in a list.

# list1= [(10, 20, 40), (40, 50, 60), (70, 80, 90)]
# list2=[]
# for i in list1:
#     l =list(i)
#     l[-1]=100
#     list2.append(tuple(l))
# print(list2)
# Expected Output: [(10, 20, 100), (40, 50, 100), (70, 80, 100)]
