class Employee:
    def __init__(self,name,salary):
        self.name = name
        self.salary = salary

class Devloper(Employee):
    def __init__(self,name,salary,language):
        super().__init__(name,salary)
        self.__language = language

    def show_details(self):
        print(f"Language is {self.__language}")


d1 = Devloper("Ram",39800,"Python")

print(d1.name)
print(d1.salary)
d1.show_details()


# Exercise: 

# Question 1 : Parent Method Access

class Vechical:
    def start(self):
        print("Vechical starts")

class Car(Vechical):
    def drive(self):
        print(f"Drive")

c1 = Car()

c1.drive()
c1.start()


# Question 2 : Constructor Inheritance

class Person:
    def __init__(self,name,age):
        self.name = name
        self.age = age

class Student(Person):
    def roll_no(self,roll_no):
        print(f"Roll_No: {roll_no}")

s1 = Student("Ram",12)

print(f"Name: {s1.name}")
print(f"Age: {s1.age}")
s1.roll_no(22)


# Question 3: Method Overriding

class Shape:
    def area(self):
        print("Area of shape")

class Rectangular():
    def area(self):
        print("Area of Rectangular")

class Circle(Shape,Rectangular):
    def area(self):
        print("Area of Circle")

c1 = Circle()
c1.area()


# Question 4:  Using super()

class Employee:
    def __init__(self,name,salary):
        self.name = name 
        self.salary = salary

class Manager(Employee):
    def __init__(self,name,salary,department):
        super().__init__(name,salary)
        self.department = department

m1 = Manager("Ram",230000,"It")

print(m1.name)
print(m1.salary)
print(m1.department)


# Quesetion 5: 6. Multilevel Inheritance

class Grandparent:
    def pr(self):
        print("I have own property.")

class Parent(Grandparent):
    def prop(self):
        print("I take property of grandparent")

class Child(Parent):
    def property(self):
        print(f"I take property of parent.")

c1 = Child()
c1.property()
c1.prop()
c1.pr()


