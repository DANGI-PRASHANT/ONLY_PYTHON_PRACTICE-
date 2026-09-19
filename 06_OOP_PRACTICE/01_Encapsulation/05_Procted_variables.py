# Question 1 :

class Employee:
    def __init__(self,salary):
        self._salary = salary

    def show_salary(self):
        print(f"Salary is {self._salary}")

e1 = Employee(12000)
e1.show_salary()


#Question 2:

class Person:
    def __init__(self,name):
        self._name = name

    def Show_name(self):
        print(f"Name is {self._name}")

p1 = Person("Alex")

p1.Show_name()


# Quesetion 3:

class Vechicals:
    def __init__(self,speed):
        self._speed = speed

class Car(Vechicals):
    def read_speeds(self):
        print(f"Read_speed is {self._speed}")


c1 = Car(100)
c1.read_speeds()


# Question 4:

class Parent:
    def __init__(self,value):
        self._value = value

class Child(Parent):
    def Access_value (self):
        print(f"Value is {self._value}")

c2 = Child(100)
c2.Access_value()



# Question 5:

class Bankaccount:

    def __init__(self,balance):
        self._balance = balance

    def deposit(self,amount):
        self._balance += amount

    def withdraw (self,amount):
        if self._balance < amount:
            print("Insufficent Balance")

        else:
            self._balance -= amount

    def show_details(self):
        print(f"Balance is ${self._balance}")

b1 = Bankaccount(1000)
b1.withdraw(2000)

b1.show_details()


# Question 6:

class Animal:
    def __init__(self,sound):
        self._sound = sound

class Dog(Animal):
    def uses_sound(self):
        print(f"{self._sound} is Dog sound.")


d1 = Dog("Bark")

d1.uses_sound()


# Question 7:

class Game:
    def __init__(self,score,level):
        self._score = score
        self._level = level

    def update(self,point1 , point2):
                print(f"Updated score is {self._score + point1}")
                print(f"Updated level is {self._level + point2}")
        

class Game1(Game):
    def show_details(self):
        print(f"score : {self._score} and Level : {self._level}")

    
    

g1 = Game1(122,54)


g1.update(10,1)
g1.show_details()



# Question 8:

class Account:
    def __init__(self,balance):
        self._balance = balance


class SavingAccounts(Account):
    def using_balance(self,interest):
        interest_amount = self._balance * interest
        print(f"Current_amount: {interest_amount + self._balance}")

s1 = SavingAccounts(1000)

s1.using_balance(0.02)


