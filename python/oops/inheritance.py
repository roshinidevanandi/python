# _____________________INHERITANCE________________

# The process of creating a new class from already existing class is called as inheritance
# The existing class is called as super or base or parent class
# The newly created class is class is called as sub or derived or child class
# SUPER CLASS: It is a class which is ready to give the resources to another class
# SUB CLASS: It is a class which is ready to take the resources from another class

# ADVANTAGES
# with the help of this we can extend the code
# code will be reusable
# It is used to save the time


# Types of interitance:
# 1.Single inheritance
# 2.Multi-level inheritance
# 3.Multiple inheritance
# 4.Hierarical inheritance
# 5.Hybrid inheritance

# 1.SINGLE INHERITANCE
# The process of creating a new class from a single base class
# EXAMPLE 1:

# class Parent:
#     def property(self):
#         print("give the properties to child")
# class Child(Parent):
#     def receive(self):
#         print("receives the propertie from parent")

# object=Child()
# object.property()
# object.receive()


# 2.MULTI-LEVEL INHERITANCE
# The process of deriving a class from already derived class.
# A class can inherit the properties and behavior of another class which have alreadyinherited the properties and behavior of some other class
# SYNTAX:
# class baseclass:
# ----------------
# ----------------
# class derivedclass1(baseclass):
# ----------------
# ----------------
# class derivedclass2(derivedclass1):
# ----------------
# ----------------

# EXAMPLE:
class A:
    def __init__(self,a,b):
        self.a=a
        self.b=b
    def sum(self):
        print(f"The sum of two numbers is {self.a+self.b} ")
class B(A):
    def sub(self):
        print(f"The sub of two numbers is {self.a-self.b} ")
class C(B):
    def mul(self):
        print(f"The mul of two numbers is {self.a*self.b}")
cal=C(8,6)
cal.sum()
cal.sub()
cal.mul()


