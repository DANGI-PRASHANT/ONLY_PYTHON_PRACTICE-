# Practice:

# Q6:
 
class Student:
    def __init__(self,age):
        self._age = age

    def show_details(self):
        print(f"Age: {self._age}")


s1 = Student(34)
s1.show_details()


# Q7:

class Car:
    def __init__(self,model):
        self._model = model

    def show_car_model (self):
        print(f"Car Model : {self._model}")


c1 = Car(2023)

c1.show_car_model()


# Q8:


class Employee:

    def __init__(self,salary):
        self._salary = salary

    def show_salary (self):
        print(f"Salary is {self._salary}")

e1  = Employee(23000)

e1.show_salary()


# Q9:

class Bankacoount: 
    def __init__(self,account_type):
        self._account_type = account_type


    def show_type (self):
        print(f"Account type : {self._account_type}")

b1 = Bankacoount("Saving")

b1.show_type()


# Q10:

class Laptop:
    def __init__(self,price):
        self._price = price

    def show_price (self):
        print(f"Price is {self._price}")

    def change_price(self,new_price):
        self._price = new_price


l1  = Laptop(1200000)

l1.change_price(200000)

l1.show_price()