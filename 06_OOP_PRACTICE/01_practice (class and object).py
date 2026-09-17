# Question:1

class Car:
    pass

c1 = Car()
print(type(c1))


# Question:2

class Dog:
    def __init__(self,name,breed):
        self.name = name
        self.breed = breed

d1 = Dog("Buddy","Labrador")
print(d1.name)
print(d1.breed)


# Question:3

class Book:
    def __init__(self,titile,author,price):
        self.title = titile
        self.author = author
        self.price = price

b1 = Book("Python Basic","John Smith",350)
print(f"Title: {b1.title}")
print(f"Author: {b1.author}")
print(f"Price: {b1.price}")        


# Question:4

class Rectangular:
    def __init__(self,length,width):
        self.length = length
        self.widht = width

r1 = Rectangular(12,22)
print(r1.length)
print(r1.widht)


# Question:5

class Car:
    def __init__(self,brand,color,model):
        self.brand = brand
        self.color = color
        self.model = model

    def show_details(self):
        print(f"Brand is {self.brand}.The color of car is {self.color} and Model is {self.model}")


# car1 = Car("Toyata","black",2023)  # it is a long method:
# car2 = Car("BMW","Blue",2025)
# car3 = Car("Honda","Red",2022)

# car1.show_details()
# car2.show_details()
# car3.show_details()


cars= [
    Car("Toyata","black",2023), # it is short methods:
Car("BMW","Blue",2025),          
Car("Honda","Red",2022)
]

for car in cars:
    car.show_details()



# Question:6

class Circle:
    def __init__(self,radius):
        self.radius = radius


r1 = Circle(5)
print(r1.radius)


r2 = Circle(10)
r2.radius = 10
print(r2.radius)


# Question:7

class Employee:
    def __init__(self,name,salary,department):
        self.name = name
        self.salary = salary
        self.department = department

emp1 = Employee("Ram",23000,"IT")

emp1.bonus = 5600

print(f"Name: {emp1.name}")
print(f"Salary:{emp1.salary}")
print(f"Department:{emp1.department}")
print(f"Bonus: {emp1.bonus}")


# Question:8

class Point:
    def __init__(self,x,y):
        self.x = x
        self.y = y


p1 = Point(2,3)
p2 = Point(5,7)

print(f"Point1: {p1.x},{p1.y}")
print(f"Point2: {p2.x},{p2.y}")


        