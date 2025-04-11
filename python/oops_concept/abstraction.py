# ______________________ABSTRACTION__________________

# Abstract class: If a class contains at least one abstract method
# Abstract method: A method without defination
# concrete class: If a class does not contains any abstract method
# Abstraction: it is the mechanism of only declaring methods but not instantrated Delcared methids are implemented
#  in its subclass
# we can't create an object for abstract class.we can create an object for concreate class
# To create abstract class into concreate class using inheritance concept
# To implement abstract class and abstract method we need to import module abc



# Declare abstract class:       class robo(ABC):  -->ABC: Abstract base class
                                    # ------
                                    # -----

# Declare abstact method: 

# @abstractmethod       -->decorator
# def sela(self):
        # none





# Example 1:

from abc import ABC, abstractmethod

class robo(ABC):
    @abstractmethod
    def sana(self):
        pass

class chitti(robo):
    def sana(self):
        print("hello sai")

on = chitti()
on.sana()  # This will only print "hello sai"
