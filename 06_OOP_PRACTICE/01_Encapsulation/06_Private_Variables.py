# Question1:

class Student:
    def __init__(self,marks):
        self.__marks = marks

    def show_marks(self):
        print(f"Marks is {self.__marks}")

s1 = Student(66)
s1.show_marks()


#Question 2:

class BankAccount:
    def __init__(self,balance):
        self.__balance = balance


    def deposit(self,amount):
        self.__balance += amount
        print(f"Deposit amount: {amount} ")
        print(f"Total Balance: {amount + self.__balance}")

    def withdraw(self,amount):
        if self.__balance < amount:
            print("Insufficent Balance")
        else:

            self.__balance -= amount
            print(f"Withdraw amount: {amount}")
            print(f"Total balance: {amount + self.__balance}")

    def show_details(self):
        print(f"Balance : {self.__balance}")


b1 = BankAccount(2000)
b1.show_details()
print()
b1.deposit(200)
print()
b1.withdraw(5000)


# Question 3:

class User:
    def __init__(self,password):
        self.__password = password

    def check_password (self):
        if self.__password == "Ram@123":
            print("Correct Password")
        else:
            print("Invalid username or password")


u1 = User("Ram@123")
u1.check_password()



# Question 4:

class Employee:
    def __init__(self,salary):
        self.__salary = salary

    def accesssing_salary (self):
        return self.__salary

e1 = Employee(1200)
# print(e1.__salary)  # Cannot accesss directly because it is private variables.

print(e1.accesssing_salary())


# Question 5:

class Counter:
    def __init__(self):
        self.__count = 0

    def increment (self):
        self.__count +=1

    def show(self):
      print(f"Count: {self.__count}")


c1 = Counter()

c1.increment()
c1.increment()
c1.increment()
c1.increment()
c1.increment()
c1.increment()

c1.show()



# Question 6:

class ATM:
    def __init__(self,atm):
        self.__atm = atm

    def Check_pin(self):
        if self.__atm == 1234:
            print("Correct PIN")

        else:
            print("Incorrect PIN")

a1 = ATM(1234)
a1.Check_pin()


# Question 7:

class Student:
    def __init__(self,marks):
        self.__marks = marks
        

    def average(self):
        total =  sum(self.__marks) / len(self.__marks)
        return total

    def rejects (self):
        for mark in self.__marks:
            if mark <0 or mark > 100:
                print("invalid input")
         

    def show_marks(self):
        print(f"average marks: {self.average()}")

s1 = Student([40,55,89,90])
s1.rejects()
s1.show_marks()


# Question 8:

class Student:
    def __init__(self,name):
        self.name = name 

s1 = Student("ram")  

s1.__name = "shyam" # it is due to name mangling .
print(s1.__name)  




