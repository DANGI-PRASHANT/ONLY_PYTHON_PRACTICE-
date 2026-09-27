# simple use of abstraction with example:

class Phone:
    def call(self):
        self.connect_network()
        print("calling...")

    def connect_network(self):
        print("Connecting network...")

p1 = Phone()
p1.call()

 # Another example:

class Bank:
    def call(self):
        self.connect_Bank_system()
        print(f"Processing...")

    def connect_Bank_system(self):
        print("connecting bank system....")

b1 = Bank()
b1.call()


# Using abstraction concept in real design : 


class BankAccount:
    def __init__(self,balance):
        self.__balance = balance

    def deposit(self,amount):
        self.__balance += amount

    def withdraw(self,amount):
        self.__balance -= amount

    def show_details(self):
        print(f"Your current balance is {self.__balance}")


b1 = BankAccount(5000)

b1.deposit(1200)
b1.withdraw(1200)
b1.show_details()


# Example of ABC Modules:

from abc import ABC,abstractmethod

class Animals(ABC):
    @abstractmethod
    def sound(self):
        pass

class Dog(Animals):
    def sound(self):
        print("Dog Barks")

class Cat(Animals):
    def sound(self):
        print("Cats Meows")


c1 = Cat()
d1 = Dog()
d1.sound()
c1.sound()


# Another example of ABC modules:

from abc import ABC , abstractmethod

class Teacher(ABC):
    @ abstractmethod
    def learn(self):
        pass

class Student_1(Teacher):
    def learn(self):
        print("Learn english language.")

class Student_2(Teacher):
    def learn(self):
        print(f"I am a student and learn python")

class Student_3(Teacher):
    def learn(self):
        print(f"I am also learn python")


students = [Student_1(),Student_2(),Student_3()]

def show_details(item):
    item.learn()

for student in students:
    show_details(student)