# _____________________INHERITANCE________________

# The process of creating a new class from already existing class is called as inheritance
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

class Parent:
    def property(self):
        print("give the properties to child")
class Child(Parent):
    def receive(self):
        print("receives the propertie from parent")

object=Child()
object.property()
object.receive() 