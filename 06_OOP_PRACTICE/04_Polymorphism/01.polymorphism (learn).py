class Dog:
    def sound(self):
        print("Dogs barks")

class Cat:
    def sound(self):
        print("Cats Meows")

d1 = Dog()
c1 = Cat()

def show(item):
    item.sound()

show(d1)
show(c1)

# Another example:

class Teacher:
    def skill (self):
        print("Teaching")

class Student:
    def skill (self):
        print('Learning and practicing')

t1 = Teacher()
s1 = Student()


def show_details(object):
    object.skill()

show_details(t1)
show_details(s1)


# Polymorphism with inheritance(method overriding style):

class Animal:
    def sound(self):
        print("This is sound of animal")

class Dog(Animal):
    def sound(self):
        print("Dogs Barks")

class Cat(Animal):
    def sound(self):
        print("Cats Meows")

animals = [Animal(),Dog(),Cat()]

# for animal in animals:
#    animal.sound() 


def produce_sound(object):
    object.sound()

for animal in animals:
    produce_sound(animal)


# Another Example:

class Employee:
    def work(self):
        print("I am employee and i do work in my sector.")

class Developer(Employee):
    def work(self):
        print("i develop websites.")

class Designer(Employee):
    def work(self):
        print("I make outerlayer design in website.")


Employees = [Employee(),Developer(),Designer()]

def do_work(Item):
    Item.work()

for employee in Employees:
    do_work(employee)


# Duck Typing:

class Bird:
    def fly(self):
        print("Bird fly")

class Aeroplane:
    def fly(self):
        print("Aeroplane fly")

def do_fly(item):
    item.fly

b1 = Bird()
a1 = Aeroplane()

do_fly(b1)
do_fly(a1)