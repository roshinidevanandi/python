# _________________CLASS_______________

# Class is ablue print of an object
# Class can be defined as a collcetion of objects
# It is a logical entity
# It is a model to create an object
# Class is a template to create an object

# Syntax

# class class_name:
    #variable declaration (instance variable)
    # method or function declaration

# ____________OBJECT________

# Object is a instance of a class
# It is an entity that existing in the real world
# It is a physical entity

# Syntax

# object_name=class_name()


# Examples:

# class         object
# car           BMW, Tata,Skeda.......
# mobile        Redmi,Vivo,oppo.....
# fruits        Banana,Apple,Orange....
# dress         tops,chudidhars,jeans.....





# Types of variables
# Public
# Private

# Public Variables
# We can access it in anywhere
# example:  x=90

# Private Variables
# We can access within a class only.if you use outside the class you'll get an error
# example:  _ _x=90 (we have to declare it with two underscores)

# SELF->self is a implicit reference if you want to access the instance variables we have to use self

# Example 1:

# class Add:
#     x=100
#     y=200

#     def sum(self):
#         print(f"Addition of two numbers is {self.x+self.y}")
    
# obj1=Add()
# obj1.sum()



# Example 2:

# class Car:
#     def __init__(self,name,brand,color):
#         self.name=name
#         self.brand=brand
#         self.color=color
#     def details(self):
#         return f"this is a {self.name} car from {self.brand} of color {self.color}"

    

# new_car1=Car("fortuner","toyota","black")
# new_car2=Car("s-cross","suzuki","white")

# print(new_car1.details())
# print(new_car2.details())



# Example 3:

# class Animal:
#     def __init__(self,name,species,sound):
#         self.name=name
#         self.species=species
#         self.sound=sound

#     def make_sound(self):
#         print(f"{self.name} the sound says: {self.sound}")

#     def describe(self):
#         print(f"{self.name} is the {self.species}")

# Animal1=Animal("Leo","Lion","Roar")
# Animal2=Animal("Milo","Cat","Meow")

# Animal1.describe()
# Animal1.make_sound()

# Animal2.describe()
# Animal2.make_sound()


# Example 4:

# class Fruit:
#     def __init__(self,name,colour,taste):
#         self.name=name
#         self.colour=colour
#         self.taste=taste
#     def describe(self):
#         return f"The {self.name} is {self.colour} and the taste is {self.taste}"
    
# Fruit1=Fruit("Apple","Red","Sweet")
# Fruit2=Fruit("Lemon","Yellow","Sour")
# Fruit3=Fruit("Ogange","Orange","Sweet and Sour")

# print(Fruit1.describe())
# print(Fruit2.describe())
# print(Fruit3.describe())