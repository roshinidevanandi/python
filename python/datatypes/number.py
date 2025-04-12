# _______________NUMBER DATA TYPES_____________

# int
# float
# complex

# print(type(342))
# print(type(6.4))
# print(type(9+2j))


# print(id(9))

# Methods

# abs

# print(abs(-659.000000))

# pow
# print(pow(3,4))

# round
# print(round(498.56))
# print(round(498.56,1))


# divmod
# print(divmod(15,5))


# Find the given number is armstrong number or not  

# ex:a=153  --->total length is 3 --> b=1pow3 + 5pow3 + 3pow3==153 -->if a==b is true the given number is armstrong number



# num=153
# copy=num
# sec=num
# count=0

# while num!=0:
#     digit=num%10
#     num=num//10
#     count+=1
# print(count)   


# sum=0
# while copy!=0:
#     digit=copy%10
#     sum=sum+digit**count
#     copy=copy//10



# if sec==sum:
#     print("It is an armstrong")

# else:
#     print("Not armstrong")



# Find the maximum of three numbers

# n1=3
# n2=25
# n3=99

# if n1>n2 and n1>n3:
#     print(f"maximum number is {n1}")
# elif n2>n3 and n2>n1:
#     print(f"maximum number is {n2}")
# else:
#     print(f"maximum number is {n3}")


# or

# def max_of_three(a, b, c):
#     return max(a, b, c)

# # Example
# print(max_of_three(12, 25, 9))  # Output: 25

  



# "Write a program to print all prime numbers between 1 and 100."

# for i in range(2, 101):  # Start from 2, since 1 is not a prime
#     is_prime = True
    
#     for j in range(2, i):
#         if i % j == 0:
#             is_prime = False
#             break
            
#     if is_prime:
#         print(i)
