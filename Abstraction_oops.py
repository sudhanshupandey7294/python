"""
ABSTRACTION
hide complexity , show functionality
It means hiding the implemenations details and showing the essential features of an object

Non-Technical Example:-
CAR
- We use the steering wheel , accelerator and brake to drive.
- We don't need to know how the engine works internally.

from abc import ABC , abstractmethod
class Animal(ABC):
    @abstractmethod
    def sound(self):
        print("Hello India")

class Dog(Animal):
    def run(self):
        print("Dog Running")

class Cat(Animal):
   pass

obj=Dog()
obj.run()   # we cannot create the object of Dog() fxn as it inherit the Animal class which is already an abstact class so we need to overeride its sound fxn insubclass also


from abc import ABC , abstractmethod
class Animal(ABC):
    @abstractmethod
    def sound(self):
        print("Hello India")

class Dog(Animal):
    def sound(self):
        print("Bark")
    def run(self):
        print("Dog Running")

class Cat(Animal):
    def sound(self):
        print("Meow")

obj = Dog()
obj.run()
obj.sound()
obj = Cat()
obj.sound()
# obj = Animal()     Cann't Instantiate we cannot make object of an abstract class

# Abstraction hides implementation details and expose only the essential interface
# Python implements abstraction using the abc module , ABC and @abstractmethod
# Abstract classes cannot be instantiated
# Subclasses must implement all abstract methods before they can be instantiate
# Abstract class can still have constructors , attributes and concrete (normal) methods
# Abstract method should not have any definition


from abc import ABC , abstractmethod
class RBI(ABC):
    @abstractmethod
    def documentation(self):
        pass

class SBI(RBI):
    pass
class PNB:
    pass
class AXIS:
    pass

acc = SBI()

"""









