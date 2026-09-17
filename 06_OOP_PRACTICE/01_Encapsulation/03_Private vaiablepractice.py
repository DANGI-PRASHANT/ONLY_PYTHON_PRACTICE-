# Private Variables:
# Q11:

class Student:
    def __init__(self,marks):
        self.__marks = marks

    def show_details(self):
        print(f"Marks is {self.__marks}")


s1 = Student(12)
s1.show_details()


# Q12:

class Bank:
    def __init__(self,balance):
        self.__balance = balance

    def show_balance(self):
        print(f"Balance is ${self.__balance}")


b1 = Bank(12000)
b1.show_balance()


# Q13:
class Employee:
    def __init__(self,salary):
        self.__salary = salary

    def show_salary(self):
        print(f"salary is {self.__salary}")

e1 = Employee(12000)
e1.show_salary()
