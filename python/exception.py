# --------------------EXCEPTION HANDLING--------------------

# when we are working on any project, we will get an errors but in python it is an interpreted language
# so the code will be executed line by line if we get an error the code won't run. It will be stopped
# so to handle those kind of errors we have an exception handling concept

# In exception handling if you get any error it will by handled by the methods
# those methods are
# try
# except
# else
# finally



# try:
#     nums=[1,2,3,4,5,6,7,8,9]
#     print(nums[8])
#     print("try block")
# except:
#     print("code can't be executed")

# finally:
#     print("it will always execute")


# 1.find the count of vowels in the given string

# try:
#     str="This is the python class started already"

#     vowels="aeiouAEIOU"

#     count=0

#     for i in range(len(str)):
#         if str[i] in vowels:
#             count+=1
#     if count==0:
#         raise Exception("No vowels available here")
#     else:
#         print(count)

# except Exception as err:
#     print("error",err)



# 2.find the given age is correct or not 

# try:
#     age=int(input("Enter the age:  "))
#     if age<0:
#         raise Exception("Incorrect age given")
#     else:
#         print(age)

# except Exception as e:
#     print(e)



# STRING FORMATING

# Definition and Usage
# The format() method formats the specified value(s) and insert them inside the string's placeholder.

# The placeholder is defined using curly brackets: {}. Read more about the placeholders in the Placeholder section below.

# The format() method returns the formatted string.


# def string_frmt(a,b):
#     print(f"the multiplication is {a*b}")

# string_frmt(6,9)


