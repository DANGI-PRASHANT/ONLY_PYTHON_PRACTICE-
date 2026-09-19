# Question.1:

class Student:
    def __init__(self,name):
        self.name = name

s1 = Student("Alex")
print(s1.name)

# Question.2:

class Car:
    def __init__(self,color):
        self.color = color


c1 = Car("Black")

print(c1.color)


# Question.3:

class Book:
    def __init__(self,title,price):
        self.title = title
        self.price = price

b1 = Book("Python","120")

print(b1.price)
print(b1.title)


#  Question.4:

class Employee:
    def __init__(self,salary):
        self.salary = salary

e1 = Employee(1200)

print(e1.salary)


# Question.5:

class Student:
    def __init__(self,name ,marks):
        self.name = name
        self.marks = marks

    def show_name(self):
        print(f"Student Name : {self.name}")

    def average_marks(self):
        return sum(self.marks) / len(self.marks)


s1 = Student("Ram",[89,76,66,55])

s1.show_name()
print(f"Average Marks : {s1.average_marks()}")



# Question.6:

class Bankaccount:

    def __init__(self,balance):
        self.balance = balance

    def show_balance(self):
        print(f"Balance is {self.balance}")

    def deposit(self,amount):
        self.balance += amount

    def withdraw (self, amount):
        if amount > self.balance:
            print("Insufficent Balance")

        else:
            self.balance -= amount

    def change_balance(self,new_balance):
        self.balance = new_balance


b1 = Bankaccount(2000)


b1.change_balance = 3000
print(f"change balance is {b1.change_balance}")

b1.deposit(1000)
b1.withdraw(20000)

b1.show_balance()


# Question.7:


class Person:
    def __init__(self,age):
        self.age = age

p1 = Person(12)
p2 = Person(45)

print(p1.age)
print(p2.age)

#Question.9:

class Temperature:
    def __init__(self, celsius):
        self.celsius = celsius

    def change(self):
        fahrenheit = (self.celsius * 9/5) + 32
        return fahrenheit


t1 = Temperature(10)

print(t1.change())


# Question 10:

class Person:
    def __init__(self, age):
        self.age = age


person = Person(25)

person.age = -50

print(person.age)