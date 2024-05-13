# # # # # Data Types:
# # # # #
# # # # # int
# # # # # string --- '' or ""
# # # # # float 1.854
# # # # # complex
# # # #
# # # # a='a+b+c+d+e+f'
# # # # c=1j+1
# # # # print(complex(c))
# # # # s=str(2j+1+1j-3j)
# # # # print(type(s))


# # # # String
# # # # -data type
# # # # collection module
# # # # "sequence of charaters"
# # # # Immutable
# # # # Ordered




# # # # #complex()

# # #  # collections:
# # # # string: Ordered & Immutable Collection Of Characters
# # # # """
# # # s1='Students of this batch are going to rock the INDIAN software industry!'
# # # # find the index of 'S'
# # # # find the index of '!'
# # # # find the index of 'I'
# # # # find the index of third space that comes between this and batch

# # # # # index: 	 0123456789..................
# # # # # -ve index
# # # # # :	 ......................................................987654321

# # str1 = "student life is best"
# # print(str1[:9:-1])


# # # [start:stop:steps/direction]

# # # # print(s1[-1])
# # # # print(s1[69])
# # # # # print(type(s1))
# # # # print(s1)
# # # # s1[0]='1'
# # # # print(s1)
# # # # # print(s1[len(s1)-1])
# # # # s2=s1[::69]
# # # # print(s2)
# # # # s2=s1[:7:2]
# # # # print(s1[:7:2])
# # # # print(s1)
# # # # print(s2)

# # # s1='Students of this batch are going to rock the INDIAN software industry!'
# # # print(s1[-25:-19:-1])

# # # print([0:101:2])


# # # # print(s1[15:6:-2])

# # # print(s1[-7:-5:-2])







# # # # start from 5 end should be till 15

# # # s1='ROYAL TECHNOSOFT limited'

# # # # ROYAL
# # # # TECHNOSOFT
# # # # limited
# # # # ROYAL limited


# # # # functions vs methods


# # # # print(type(s1))
# # # # print(len(s1)-1)


# # # # # methods:
# # s1='rOYAL TECHNOSOFT limited. i'

# # # print(s1)
# # print(s1.capitalize())
# # print(s1.upper())
# # print(s1.lower())
# # print(s1.swapcase())
# # print(s1.title())

# # s1='students .of this batch are going to rock the INDIAN software industry!'

# # output: s1 capitilize
# #         indian in lower case
# #         all the s1 string should in upper case
# #         all the s1 string should be in lower case
# #         software industry  in uppercase


# s1 = 'DtDudents of this batch are going to rock the INDIAN software industry?'
# s2 = "What is ß"

# print(s2.lower())
# # print(s1)
# print(s1.casefold())


# alignment methods

s1 = 'Students of this batch are going to rock the INDIAN software industry?'
print(len(s1))
# print(s1.center(150,"*"))
print(s1.rjust(10, "*"))
print(s1.ljust(100, "-"))
# # # # print(s3)
# # # # Alignment related methods
# # # """
# # # s3 = s1.center(100)
# # # print(s1.center(100, "-"))
# # # s1='11'
# # # print(s1.rjust(100))
# # # print(s1.ljust(100, "-"))
# # #
# # # print("-" * 102)
# # # print("|" + "Welcome to our software!".center(100) + "|")
# # # print("-" * 102)
# # # """
# # #
print("|" + "Welcome to our software!".center(100) + "|")
# #
# #
# #
# # # print(s1.count("e e",10,20))
# # # print(s1.count("are"))
# # # print(s1.count("europe"))
# # #
# # # print(s1.count("z", 20))
# # # print(s1.count("e", 20, 40))
# # # print(s1.count("e", -40, -20))
# # s1 = 'stDudents of this batch are going to rock the INDIAN software industry?'
# # # print(s1.count('aeiou',10,100))
# # print(s1)
# # s2=s1.encode('utf-16')
# # print(s2)
# # print(type(s2))
# # print(s2.decode('utf-16'))
# #


# # print(s1.encode())
# # print(s1.encode("utf-16"))

# s1='students of this batch are going to rock the INDIAN software industry?'
# # print(s1.endswith("?",10,20))
# # print(s1.endswith("try!"))
# # print(s1.endswith("is", 40))
# # s1.endswith("s", 40, 60)


# # print(s1.startswith("S",10,20))
# # print(s1.startswith("t", 1,3))


# s1='students Dof this batch are going to rock the INDIAN softwaDre industry?  '



# # print(s1.split(' '))
# # print('-'.join(s1))

# print('*'.join(s1.split()))
# # print(s1.find("D"))
# # # print(s1.find("e"))
# # print(s1.index("D"))
# #
# # print(s1.rfind("D"))
# # # print(s1.lfind("D"))
# # print(s1.rindex("D"))
# # print(s1.lindex("D"))

# """
# print(s1.find("D"))
# print(s1.find("e"))
# print(s1.find("rock"))

# a = s1.find("e")
# print(s1.find("e", a+1))

# print(s1.find("e", 5))
# print(s1.find("e", 5, 30))

# print(s1.find("e", 5, -5))
# print(s1.find("Python"))

# print()

# print(s1.index("D"))
# print(s1.index("e"))
# print(s1.index("rock"))

# a = s1.index("e")
# print(s1.index("e", a+1))

# print(s1.index("e", 5))
# print(s1.index("e", 5, 30))

# print(s1.index("e", 5, -5))
# print(s1.index("Python"))


# print(s1.rfind("e"))
# print(s1.rfind("are", 20, -3))
# print(s1.rindex("D"))
# print(s1.rindex("r", 20, -20))
# """

