# Public variables:
# Example:

class Student:
    def __init__(self,name):
        self.name = name

s1 = Student("Ram")
print(s1.name)


class Vechical:
    def __init__(self,age):
        self.age = age

v1 = Vechical(12)
print(v1.age)


# Q1. 

class Student:
    def __init__(self,name ):
        self.name = name

s1 = Student("ram")
print(s1.name)

# Q2: 

class Car:
    def __init__(self,brand):
        self.brand = brand


c1 = Car("Toyata")
print(c1.brand)


# Q3: 

class Book:
    def __init__(self,title):
        self.title = title

b1 = Book("Python Basic")
print(b1.title)


# Q4:

class Employee:
    def __init__(self,name):
        self.name = name

    def show_details(self):
        print(f"My name is ")

    def change_name(self,new_name):
        self.change_name = new_name

e1 = Employee("Ram")

e1.change_name("shyam")
print(e1.change_name)


# Q5:

class Mobile:
    def __init__(self,model):
        self.model = model

    def show_details(self):
        print(f"Model : {self.model}")

m1 = Mobile(2023)
m2 = Mobile(2026)

m1.show_details()
m2.show_details()
