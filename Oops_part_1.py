
'''
# OOPs (Object Oriented Programming)
# Main Components =>  Class , Object
# 4 Main Pillars => Encapsulation , Polymorphishm , Inheritance , Abstraction

# class :- class is a virtual entity (it is blue print of an object)
# class is the representation of encapsulation
Syntax:-
class class_name:
    class's_property

# class properties :- Data Member , Member Functions
'''
#Example

class myclass:
    a=10
    b=20
    def myfunction():
        print("I am in myclass")

class classA:
    x=100
    def myfunctionA():
        print("I am in classA")

#print(x)  # give error since Class is a virtual entity it is not realistic so we cannot print 'x' directly from inside a class we need to call it by :
           # class_name.x

print(classA.x)
classA.myfunctionA()

#__________________________________________________________________________________________    
# object:- Object is a real world entity
# self :- self is the current class's object used to call a class

class classA:
    x=0
    y=0
    def input(self,a,b):
        self.x=a
        self.y=b
        self.add()

    def add(self):
        z=self.x+self.y
        print("Addition: ", z )

classA().input(10,20)     # using ClassA() with () means we are calling the class by object

#______________________

class classA:
    x = 0
    y = 0
    def input(self,a,b):
        self.x = a
        self.y = b
        self.add()
    def add(self):
        z = self.x+self.y
        print("Addition :",z)

obj = classA()    
obj.input(10,20)

#_____________________________________________________
# decorator:- decorator is a functionality of a method from which a method
#get some special feature

class classA:
    x = 0
    y = 0
    def input(self,a,b):
        self.x = a
        self.y = b
        self.add()
    def add(self):
        z = self.x+self.y
        print("Addition :",z)
    def welcome(self):
        print("Welcome to my service class 'CLASSA'")
obj = classA()    
obj.welcome()  # it give error because we dont given any object to the welcome fxn..and still we are calling it using obj.welcome  ..we have to give "self" then it will run
obj.input(10,20)


class classA:
    x = 0
    y = 0
    def input(self,a,b):
        self.x = a
        self.y = b
        self.add()
    def add(self):
        z = self.x+self.y
        print("Addition :",z)
    def welcome(self):
        print("Welcome to my service class 'CLASSA'")

obj=classA()
obj.welcome() # now , it will run because we have give it an object "self"

## but here comes decorator in play , using decorator --> "@staticmethod" on a method which is inside a class .. then we don't need to pass ''self" as an object the @staticmethod make the
# function of a class static and give it a real entity like feeling ..so that it forget that it is a virtual entity inside a class
#example------

class classA:
    x = 0
    y = 0
    def input(self,a,b):
        self.x = a
        self.y = b
        self.add()
    def add(self):
        z = self.x+self.y
        print("Addition :",z)
    @staticmethod                    # we dont need "self" to call welcome() fxn
    def welcome():
        print("Welcome to my service class 'CLASSA'")


obj=classA()
obj.welcome()

#_________________________________________________________________________________________
# Constructor :- Constructor is a functionality of a class's method
# where this method will automatically called when an object will be created!
# constructor method's name should be __init__

class classA:
    def myfunction(self):
        print("I am myfunction")
    def __init__(self):
        print("I am __init__")

obj = classA()  #Use __init__(), function will automatically called just by calling its class no need to call it by creating its object, it is constructor..
obj.myfunction()  


