# Question 18:

class Animals:
    def eat(self):
        print("Eating")

class Bird(Animals):
    def fly(self):
        print("Fly")

class Parrot(Bird):
    def talk(self):
        
        print(f"talk")

p1 = Parrot()

p1.talk()
p1.eat()
p1.fly()


# Question 19:

