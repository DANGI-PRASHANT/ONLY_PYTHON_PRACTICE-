# Practice:

class Student:
    def __init__(self,marks):
        self.__marks = marks

    def gets_marks(self):
        return self.__marks

class Result(Student):
    def show_result(self):
        if self.gets_marks() >=40:
            print(f"Marks:{self.gets_marks()}")
            print(f"Result: Pass")

        else:
            print("Result: Fail")

r1 = Result(84)

r1.show_result()



# Practice 3:

class Employee:
    def __init__(self,salary):
        self.__salary = salary


    def get_salary(self):
        return self.__salary


class Manager(Employee):
    def add_bonus(self,Bonus):
        print(f"Salary : {self.get_salary()}")
        print(f"Bounus: {Bonus}")
        print(f"Total_salary: {self.get_salary() + Bonus}")

m1 = Manager(50000)

m1.add_bonus(5000)



# Practice 4:

class Product_price:
    def __init__(self,price):
        self.__price = price

    def get_price(self):
        return self.__price


class Discountproduct(Product_price):
    def discount(self,percent):
        print(f"Price: {self.get_price()}")
        discount = percent*self.get_price()
        print(f"Discount: {discount}")
        print(f"Final Price: {self.get_price() - discount}")

d1 = Discountproduct(1000)

d1.discount(0.1)

# Challenge question:

class BankAccount:

    def __init__(self, balance):
        self.__balance = balance

    def deposit(self, amount):
        self.__balance += amount
        print(f"Deposit: {self.__balance}")

    def get_balance(self):
        return self.__balance

    def withdraw(self, amount):
        self.__balance -= amount
        print(f"Withdraw: {self.__balance}")


class SavingAccount(BankAccount):

    def add_interest(self, rate):
        interest = self.get_balance() * rate

        print(f"Interest: {interest}")
        print(f"After Interest: {self.get_balance() + interest}")


save = SavingAccount(5000)

print(f"Initial Balance: {save.get_balance()}")

save.deposit(1000)

save.withdraw(1000)

save.add_interest(0.1)



