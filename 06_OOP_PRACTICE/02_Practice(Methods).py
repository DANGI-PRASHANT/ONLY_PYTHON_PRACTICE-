# Question 13: Create a class called Greeter with a method say_hello() that prints "Hello!" when called. Create an object and call the method.

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

class Student:

    def get_students(self):
        students = input("Enter student names: ").split()
        return students


s1 = Student()

result = s1.get_students()

print(result)

