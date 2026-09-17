# Question 13: 

class Greeter:
    def number(self):
        print("say_hello")

g1 = Greeter()
g1.number()

# Question 14: 

class Student:
    def __init__(self,name,age):
        self.name = name
        self.age = age

s1 = Student("Anita",22)

print(s1.name)
print(s1.age)

# Question 15:

class Calculator:
    def add (self,a,b):
        return a+b

c1 = Calculator()

result = c1.add(4,5)
print(result)


# Question 16: 

class Circle:
    def __init__ (self,radius):
        self.radius = radius

    def area(self):
        return 3.14*self.radius*self.radius

c1 = Circle(2)

result = c1.area()
print(result)


# Question 17:

class Rectangular:
    def __init__(self,length,width):
        self.length = length
        self.width = width

    def area(self):
        return self.length * self.width

    def perimeter (self):
        return 2*(self.length + self.width) 


r1 = Rectangular(6,3)

result1 = r1.area()
result2 = r1.perimeter()

print(f"Area: {result1}")
print(f"Perimeter: {result2}")



# Question 18:

class Employee:
    def __init__(self,name,salary):
        self.name = name
        self.salary = salary

    def give_raise(self,amount):
        

        self.salary += amount


e1 = Employee("Ram",30000)

e1.give_raise(5000)
print(e1.salary)


# Question 19:

class Counter:
    def __init__(self,count):
        self.count = 0

    def increment (self):
        self.count += 1

c1 = Counter(2334)
c1.increment()
c1.increment()
c1.increment()

print(c1.count)


# Question 20:

class Temperature:
    def __init__(self,celsius):
        self.celsius = celsius

    def to_fahrenheit(self):
        return (self.celsius * 9/5) + 32 

t1 = Temperature(12)

result = t1.to_fahrenheit()
print(result)


# Question 21:

class ShoppingCart:
    def __init__(self):
        self.items = []

    def add_item(self, item):
        self.items.append(item)

    def show_items(self):
        for item in self.items:
            print(item)


cart = ShoppingCart()

cart.add_item("Book")
cart.add_item("Pen")
cart.add_item("Bag")

cart.show_items()


# Q22:

class Bankaccount:
    def __init__(self,balance):
        self.balance = balance

    def withdraw (self,amount):
        if amount >= self.balance:
            print("Insufficent Balance")

        else:
            self.balance -= amount

    def deposit (self,amount):
        self.balance += amount

    def show_details(self):
       print(f"Balalnce is ${self.balance}")

b1 = Bankaccount(20000)
b1.deposit(12000)
b1.show_details()



# Q23:

class Student:
    def __init__(self,name,marks):
        self.name = name
        self.marks = marks
    

    def average(self):
        return sum(self.marks) / len(self.marks)

s1 = Student("Ram",[80,90,70])

print(s1.average())



# sample type  of question:

class Student1:
    def __init__(self,name, age,marks):
        self.name = name
        self.age = age
        self.marks = marks


    def average1(self):
        return sum(self.marks) / len(self.marks)

    def total (self):
        return sum(self.marks)

    def percentage(self):
        total = sum(self.marks)
        percentage = (total / (len(self.marks) *100)) *100
        return percentage


s2 = Student1("Ram",12,[45,30,22,43,45,50])

print(s2.average1())
print(s2.percentage())
print(s2.total())



# Q24:

class Library:
    def __init__(self):
        self.books = []

    def add_book(self, title):
        self.books.append(title)

    def remove_book(self, title):
        self.books.remove(title)

    def total_books(self):
        return len(self.books)


library = Library()

library.add_book("Python")
library.add_book("Java")
library.add_book("C++")
library.add_book("HTML")

library.remove_book("Java")

print("Total books:", library.total_books())