# Question 1:

class Animal:
    def eat(self):
        print("This animal eats food.")

class Dog(Animal):
    def barK(self):
        print("The dog barks")

d1 = Dog()
d1.barK()
d1.eat()


# Question 2:

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age


class Student(Person):
    def add(self, roll_number):
        print(f"Roll_Number: {roll_number}")


s1 = Student("Ram", 16)
s2 = Student("Hari", 22)

print(f"Name: {s1.name}")
print(f"Age: {s1.age}")

s2.add(101)


# Question 5:

class Shape:
    def info(self):
        print('i am a shape')

class Circle(Shape):
    def area(self,radius):
        Area = 3.14*radius*radius
        print(f"Area of circle : {Area}")
        return Area
    

c1 = Circle()
c1.info()

c1.area(5)



# Question 6:


class Animal:
    def __init__(self,name):
        self.name = name 


class Dog(Animal):
    def bark(self):
        print(f"Dog barks")

d1 = Dog("sheru")
print(f"Dog_name: {d1.name}")
d1.bark()


# Question 8:

class BankAccount:
    def __init__(self, balance):
        self.__balance = balance

    def show_balance(self):
        print(f"Balance : {self.__balance}")

    def get_balance(self):
        return self.__balance


class SavingAccount(BankAccount):

    def add_interest(self, interest):
        balance = self.get_balance() * interest
        print(f"Interest_amount: {balance}")
        print(f"New Balance: {self.get_balance() + balance}")

    def show_details(self):
        self.add_interest(0.1)


s = SavingAccount(1000)

s.show_balance()
s.show_details()