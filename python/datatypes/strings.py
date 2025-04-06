# --------------STRINGS------------

# String is a collection of charectors
# It is immutable we can't change the elements and it is primitive data type
# In strings elements are accessed through the index
# It is a sequence data type



# data="helloeveryONE234"

# print(data)

# data[0]="r"    -->TypeError: 'str' object does not support item assignment


# METHODS

# upper()
# print(data.upper())

# lower()
# print(data.lower())

# swapcase()
# print(data.swapcase())


# strip()  --->it removes the spaces
# print(data.strip())

# lstrip()
# print(data.lstrip())

# rstrip()
# print(data.rstrip())


# # replace()
# print(data.replace("e","E"))
# print(data.replace("e","9"))

# isalpha()
# print(data.isalpha())

# isdigit()
# print(data.isdigit())

# isalnum()
# print(data.isalnum())

# startswith()
# print(data.startswith("h"))

# endswith()
# print(data.endswith("r"))

# find()  ->it finds the index of the element
# print(data.find("e"))

# zfill() -->zero fill
# print(data.zfill(30))

# center()
# print(data.center(30,"*"))


# for i in range(len(data)):
#     print(data[i])


# frds=" "
# isspace()
# print(frds.isspace())


# split()
# data1="i am roshini from peddapalli"
# new=data1.split()
# print("".join(new))



# ASCII ------------->>American Standard Code For Information Interchange

# 0-9  ----->48-57
# A-Z  ----->65-90
# a-z  ----->97-122

# ord
# print(ord("&"))
# print(ord("9"))
# print(ord("*"))

# chr
# print(chr(69))
# print(chr(98))
# print(chr(42))


# id  ------>To find the address of the variable
# value=98
# print(id(value))







# ________________________PROBLEM SOLVING____________________

# palindrome
# 1.find the given string is palindrom or not palindrome

# data3="racecars"
# new_data=""
# for i in range(len(data3)-1,-1,-1):
#     new_data+=data3[i]   
# if data3==new_data:
#     print(data3,"is palindrome")
# else:
#     print(data3,"is not palindrome")




# 2.find the most repeated letter in the given sentance

# string="this is the python class"

# most=""
# count=0
# for i in range(len(string)):
#     if string.count(string[i])>count:
#         most=string[i]
#         count=string.count(string[i])

# print(most)



# anagram

# 3.find the given two words are anagrams or not ANAGRAMS 

# str1="silent"
# str2="listen"

# if len(str1)!=len(str2):
#     print("not anagrams")
# else:
#     ana=True
#     for i in range(len(str1)):
#         if str1.count(str1[i])!=str2.count(str1[i]):
#             ana=False
#     if ana:
#         print(str1,str2,"are anagrams")

#     else:
#         print("not anagrams")





# ____________________________Slicing______________________

str3="hello i am pupy"

# print(str3[::])
# print(str3[:5:])
# print(str3[:5:2])
# print(str3[5:])
# print(str3[5:60])
# print(str3[::-1]) ------>for reverse of the str


# palindrome        

# str="rar"
# print(str==str[::-1])



