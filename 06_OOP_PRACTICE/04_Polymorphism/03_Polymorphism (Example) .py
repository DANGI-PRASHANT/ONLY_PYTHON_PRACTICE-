# Question 1 : 1. Method Overriding (Basic)

class Animal:
    def sound(self):
        print("Animals produce sound")

class Dog:
    def sound(self):
        print(" Dog Barks")

class Cat:
    def sound(self):
        print("Cats Meows")

animals = [Animal(),Dog(),Cat()]

def produce_sound(item):
    item.sound()

for animal in animals:
    produce_sound(animal)

# Question 2 : Same Method Name, Different Output

class Car:
    def fuel(self):
        print("Petrol")

class Bike:
    def fuel(self):
        print("Petrol or Electric")

vechicals = [Car(),Bike()]

def feature(item):
    item.fuel()

for vechical in vechicals:
    feature(vechical)


# Question 3 : Function Polymorphism

class Dog:
    def sound_1(self):
        print("Dog barks")

class Cow:
    def sound_1(self):
        print("Cow Baaaa")

d1 = Dog()
c1 = Cow()


def show_sound(animal):
    animal.sound_1()

show_sound(d1)
show_sound(c1)


