# i=6
# if i==6:
#     print("hello world")



# i=2
# if i==2:
#     print("yaah")
# else:
#     print("not a valid number")




# num=int(input("enter your liked number: "))
# if num==1:
#     print("sunday")
# elif num==2:
#     print("monday")
# elif num==3:
#     print("tuesday")
# elif num==4:
#     print("wednesday")
# elif num==5:
#     print("thursday")
# elif num==6:
#     print("friday")
# elif num==7:
#     print("saturday")
# else:
#     print("invalid number")




# 1. Check if a number is positive, negative, or zero:
# Write a Python program that takes an integer input and prints whether the number is positive, negative, or zero.

# Example input/output:

# Input: 5 Output: Positive number
# Input: -3 Output: Negative number
# Input: 0 Output: Zero




# num=int(input("enter the number:"))
# if num>0:
#     print("positive number")

# elif num<0:
#     print("negative number")
# else:
#     print("zero")





# 3. Grade Calculator:
# Write a program that asks the user to input a student's score and prints the corresponding grade based on the following criteria:

# A for scores 90 or above
# B for scores between 80 and 89
# C for scores between 70 and 79
# D for scores between 60 and 69
# F for scores below 60
# Example input/output:

# Input: 85 Output: Grade: B
# Input: 72 Output: Grade: C
# Input: 45 Output: Grade: F




# marks=int(input("enter the marks: "))
# if marks>=90:
#     print("Grade: A")
# elif marks<=89 and marks>=80:
#     print("Grade: B")
# elif marks<=79 and marks>=70:
#     print("Grade: C")
# elif marks<=69 and marks>=60:
#     print("Grade D")
# else:
#     print("Grade: F")





# 4. Odd or Even Number Checker:
# Write a program that checks if a given number is odd or even.

# Example input/output:

# Input: 6 Output: Even number
# Input: 7 Output: Odd number



# num=int(input("enter the number here: "))
# if num%2!=1:
#     print("even")
# else:
#     print("odd")



# 5. Vowel or Consonant Checker:
# Write a program that takes a character as input and checks whether it is a vowel (a, e, i, o, u) or a consonant.

# Example input/output:

# Input: a Output: Vowel
# Input: b Output: Consonant




# letters=input("enter the letter here: ")
# if letters=="a" or letters=="e" or letters=="i" or letters=="o" or letters=="u":
#     print("Vowel")
# else:
#     print("Consonant")





# 6. Check if a Number is Divisible by Both 3 and 5:
# Write a Python program to check if a given number is divisible by both 3 and 5.

# Example input/output:

# Input: 15 Output: Divisible by both 3 and 5
# Input: 9 Output: Not divisible by both 3 and 5




# num=int(input("enter the number: "))
# if num%3==0 and num%5==0:
#     print("Divisible by both 3 and 5")
# else:
#     print("Not divisible by both 3 and 5")









# 7. Weekend or Weekday Checker:
# Write a program that asks the user to input a number between 1 and 7. Based on the number, the program should print if it's a weekday or weekend:

# Numbers 1 to 5 represent weekdays.
# Numbers 6 and 7 represent weekends.
# Example input/output:

# Input: 3 Output: Weekday
# Input: 7 Output: Weekend




# num=int(input("enter the number: "))
# if num==6 or num==7:
#     print("Weekend")
# else:
#     print("Weekday")




# 8. Check if a Number is Prime:
# Write a program that checks if a given number is prime. A prime number is a number greater than 1 that has no divisors other than 1 and itself.

# Example input/output:

# Input: 7 Output: Prime number
# Input: 10 Output: Not a prime number



# fact=0
# num=int(input("enter the number here: "))
# for i in range(1,num+1):
#     if num%i==0:
#         fact+=1
# if fact>2:
#     print("Not a Prime Number")
# else:
#     print("Prime Number")








# 10. Check if a Number is Palindrome:
# Write a Python program to check if a given number is a palindrome. A palindrome number is a number that remains the same when its digits are reversed.

# Example input/output:

# Input: 121 Output: Palindrome
# Input: 123 Output: Not a palindrome








# num=input("enter the number here:")
# num_res=num[::-1]
# print(num_res)
# if num==num_res:
#     print("Palindrome")
# else:
#     print("Not Palindrome")





