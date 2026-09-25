# Challenge 3 _Student Marks:

class Student:
    def __init__(self,marks):
        self.__marks = marks

    def get_marks(self):
        print(f"Inital Marks:{self.__marks}")

    def add_marks(self,add):
        Bonus = self.__marks +add
        print(f"Bonus Marks: {add}")
        print(f"After Bonus : {Bonus}")

  

    def show(self):
        return self.__marks

class Class_Topstudent(Student):
    def deduct_marks(self,amount):
        total = self.show() - amount
        print(f"Deducted Marks: {amount}")
        print(f"Final Marks: {total}")


c1 = Class_Topstudent(75)

c1.get_marks()
c1.add_marks(10)
c1.deduct_marks(5)



# chanllenge 4:

class Product:
    def __init__(self,price):
        self.__price = price

    def get_price(self):
        print(f"Inital Price: {self.__price}")


    def add_discount(self,amount):
        self.__price -= amount
        print(f"Discount : {amount}")
        print(f"After Discount: {self.__price}")

    def call_price(self):
        return self.__price


class PremiumProduct(Product):
    def add_tax(self,amount):
        tax_total = self.call_price() + amount
        print(f"Tax: {amount}")
        print(f"Final price: {tax_total}")


p1 = PremiumProduct(2000)

p1.get_price()
p1.add_discount(300)
p1.add_tax(200)



# Challenge 5:

class MobileAccount:
    def __init__(self,balance):
        self.__balance = balance

    def get_balance(self):
        print(f"Initial Balance: {self.__balance}")

    def add_balance(self,amount):
        self.__balance += amount
        print(f"Added Balance: {amount}")
        print(f"After Balance: {self.__balance}")

    def show(self):
        return self.__balance

class PremiunmAcccount(MobileAccount):
    def use_balance(self,amount):
        new_balance = self.show() - amount
        print(f"Used Balance: {amount}")
        print(f"Final Balance: {new_balance}")


p2 = PremiunmAcccount(500)

p2.get_balance()
p2.add_balance(200)
p2.use_balance(150)



# Challenge 8 : More Difficult

class Employee:
    def __init__(self,salary):
        self.__salary = salary

    def show_salary(self):
        print(f"Inital Salary: {self.__salary}")

    def add_bonus(self,amount):
        self.__salary += amount
        print(f"Bonus: {amount}")
        print(f"After Bonus: {self.__salary}")

    def call_salary (self):
        return self.__salary


class Manager(Employee):
    def add_allowance(self,amount):
        self.__new_amount = self.call_salary() + amount
        print(f"Allowance: {amount}")
        print(f"After Allowance: {self.__new_amount}")

    def deduct_tax(self,amount):
        new_tax = self.__new_amount - amount
        print(f"Tax: {amount}")
        print(f"Final salary: {new_tax}")

m1 = Manager(70000)

m1.show_salary()
m1.add_bonus(10000)
m1.add_allowance(5000)
m1.deduct_tax(8000)