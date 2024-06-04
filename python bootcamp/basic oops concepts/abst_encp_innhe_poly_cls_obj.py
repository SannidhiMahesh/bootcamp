# Abstraction
# Abstraction is the process of hiding the implementation details and showing only the necessary features of an object.

class Animal:
    def speak(self):
        pass

class Dog(Animal):
    def speak(self):
        print("Woof!")

class Cat(Animal):
    def speak(self):
        print("Meow!")

# Usage
dog = Dog()
dog.speak()  

cat = Cat()
cat.speak()  


# Encapsulation
# Encapsulation is the bundling of data (attributes) and methods (functions) that operate on the data into a single unit.

class BankAccount:
    def __init__(self):
        self.__balance = 0

    def deposit(self, amount):
        self.__balance += amount

    def withdraw(self, amount):
        if amount <= self.__balance:
            self.__balance -= amount
        else:
            print("Insufficient funds")

    def get_balance(self):
        return self.__balance

# Usage
account = BankAccount()
account.deposit(100)
account.withdraw(50)
print("Current Balance:", account.get_balance())  


# Inheritance
# Inheritance allows a class (subclass) to inherit the properties and methods of another class (superclass).

class Vehicle:
    def drive(self):
        print("Vehicle is moving")

class Car(Vehicle):
    pass

# Usage
car = Car()
car.drive()  

# Polymorphism
# Polymorphism allows objects of different classes to be treated as objects of a common superclass.

class Animal:
    def speak(self):
        pass

class Dog(Animal):
    def speak(self):
        print("Woof!")

class Cat(Animal):
    def speak(self):
        print("Meow!")

# Usage
def make_sound(animal):
    animal.speak()

dog = Dog()
cat = Cat()

make_sound(dog) 
make_sound(cat)  


# Class
# A class is a blueprint for creating objects.

class Dog:
    pass

# Usage
my_dog = Dog()
print(type(my_dog))  

# Object
# An object is an instance of a class.

class Dog:
    def bark(self):
        print("Woof!")

# Usage
my_dog = Dog()
my_dog.bark()  
