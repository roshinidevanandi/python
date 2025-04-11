# _______________ENCAPSULATION_____________

# Encapsulation is a programing technique that bindes data and corresponding methods together into a single unit
# It provides data hiding and data protection
# Data protect through access specifiers
# 1.private: only inside the class and class methods
# 2.protected: inside class and its immediate subclass
# public: entire program

# Example 1:

# class robo:
#     x=99
#     def chitti(self):
#         print("hello from encapsulation")


# obj1=robo()
# obj1.chitti()
# print(obj1.x)


# Example 2:

# class robo:
#     __x=89 
#     # -->this is private variable
#     def chitti(self):
#         print(self.__x)
# obj1=robo()
# obj1.chitti()
