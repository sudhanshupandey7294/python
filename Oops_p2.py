"""
OOPs's Main Pillars
Encapsulation , Abstraction , Polymorphism , Inheritance

ENCAPSULATION
Encapsulation refers to the bundling of data with the mechanisms or
methods that operate on the data. It may also refer to the limiting of
direct access to some of that data, such as an object's components.

Encapsulation means bundling data members and member functions in a class.
class class_name:
    data_member1 = value1
    data_member2 = value2
    def member_function1():
        statements
    def member_function2():
        statements

Example:-
class classA:
    x = 100
    def myfunctionA():
        print("I am in classA")

# if you want to access any class's property you need to create an object

INHERITANCE
You can inherit a class into another so that a child class's object can
access the property of parent class
class Parent:
    service1
    serivce2

class Child(Parent):
    service3
    service4

obj = Child()
obj.service3
obj.service1


Types of Inheritance
1- Single Inheritance

class classA:
    def funA(self):
        print("I am functionA from classA")

class classB(classA):
    def funB(self):
        print("I am functionB from classB")

obj = classB()
obj.funA()

2- Multiple Inheritance

class classA:
    def funA(self):
        print("I am functionA from classA")

class classB:
    def funB(self):
        print("I am functionB from classB")

class classC(classA,classB):
    def funC(self):
        print("I am functionC from classC")


obj = classC()
obj.funA()
obj.funB()


3- Multilevel Inheritance

class classA:
    def funA(self):
        print("I am functionA from classA")

class classB(classA):
    def funB(self):
        print("I am functionB from classB")

class classC(classB):
    def funC(self):
        print("I am functionC from classC")


obj = classC()
obj.funA()
obj.funB()


4- Hierarchicle Inheritance

class classA:
    def funA(self):
        print("I am functionA from classA")

class classB(classA):
    def funB(self):
        print("I am functionB from classB")

class classC(classA):
    def funC(self):
        print("I am functionC from classC")


obj = classC()
obj.funA()
obj = classB()
obj.funA()


5- Hybrid Interitance

class classA:
    def funA(self):
        print("I am functionA from classA")

class classB(classA):
    def funB(self):
        print("I am functionB from classB")

class classC(classA):
    def funC(self):
        print("I am functionC from classC")

class classD(classB,classC):
    def funD(self):
        print("I am functionD from classD")

obj = classD()
obj.funA()
obj.funB()
obj.funC()


POLYMORPHISM
poly(many) + morphism(forms)

- Function Overloading
- Function Overriding

FUNCTION OVERLOADING

class myclass:
    def add(self,num1,num2):
        return num1+num2

obj = myclass()
print( obj.add(10,20) )           # Addition
print( obj.add("Aman","Kumar") )  # Concatenation
print( obj.add([1,2,3],[4,5,6]) ) # Extend


FUNCTION OVERRIDING

class classA:
    def function(self):
        print("I am in class A")
class classB(classA):
    def function(self):
        print("I am in class B")

obj = classB()
obj.function()

# classB's Object will access its property not its Parent property

"""
