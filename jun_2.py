# list = array 
# l1=[]
l1=[1,"1234567",1.1,[123,12345,"wer"]]

# print(l1[3][2])
# print(l1[2:5])
# l1.append(6789)
# l1.append(["6789","2345678o"])
# l1.insert(1,"1234567890")
# l1.extend("123456789")
# print(l1)

# x=l1.pop()
# l1.insert(1,x)
# print(l1)

# l1.pop(4)
# l1.remove(1.123)
# print(l1)

# l1.clear()
# print(l1)

# del l1[2:4]
# print(l1)


# conditions

# if (i>0)
#     {
#         a=1;

#     }

i=2

# if i>1:
#     print("Yes")

# print("No")

# if i == 2 or i ==1:
#     print("if")

# if i == 2 and i >1:
#  print("If")
#  print("345678")
#  print("fgh")


# if i > 1:
#     if i==2:
#       print("1")
#     else:
#         print("2")
# else:
#    if i >0:
      
#     print("3")



# if i > 2:
#     print("if")
# elif i >3:
#     print("elif 1")
# elif i == 2:
#     print("elif 2")
# else:
#     print("else")


# int(input())

# l1=["1",[2,3]]
# str1="123456789"

# if 2 in l1[1]:
#     print("yes")
# else:
#     print("NO")


# Write a  Python program to check the validity of passwords input by users.

# 1. Minimum length 6 characters.
# Maximum length 16 characters.

# 2. At least 1 character from [$#@].
                              
# 3. At least 1 number between [0-9].

# print("123".isalnum())

int_str = input("enter passdword : ")
# print(int_str.isalnum())

if len(int_str) >= 6 and len(int_str) <= 16:
    if '@' in int_str or '$' in int_str or '#' in int_str:

        for i in int_str:
                if i.isdigit():
                    print(f"{int_str} is valid")
                    break
    

# print('123@'.isdigit())
        # if i.isdigit():
        #     print("yes")
        # else:
        #     print("No")
        
        # if int_str.isalnum():
        #     print(f"your passowrd is valid : {int_str}")
#         else:
#             print("numeric num req")
#     else:
#             print("special char req")
# else:
#             print("minimun 16 max 6 required")


# for i in 'qwert7':
#     print(i)
#     if i.isdigit():
#         print("-------")
#         print("yes")
#     else:
#         continue
#         print("No")


        # if i in ['1','2','3','4','5','6','7','8','9'] or i in '1234567890':
        #     print("Hello")
        #     break
        # else:
        #     continue

