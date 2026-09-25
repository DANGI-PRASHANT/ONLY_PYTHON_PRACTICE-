# Question 10:

class Father:
    def skill(self):
        print("Gardening , cooking")


class Mother:
    def skill1(self):
        print("Cooking,Painting")

class child(Father,Mother):
    def skill2(self):
        print("Gaming")

c1 = child()

c1.skill()
c1.skill1()
c1.skill2()


# Question 12:

class Flyer:
    def fly(self):
        print("I can fly")

class Swimmer:
    def swim(self):
        print(f"I can swim")

class Duck(Flyer,Swimmer):
    def both(self):
        print("I can swim and fly")






d1 = Duck()

d1.fly()
d1.swim()
d1.both()


# Question 15: ( MEthod Resolution Order)

class Walker:
    def move(self):
        print("walking")

class Runner:
    def move(self):
        print(f"Runnning")

class Athlete(Runner,Walker):
    pass

a = Athlete()

a.move()


# Question 14:

class Engine:
    def start_engine(self):
        print("start engine")

class Musicsystem:
    def play_music(self):
        print("Play music")

class car(Engine,Musicsystem):
    pass

c1 = car()

c1.start_engine()
c1.play_music()


# Question 16:

class Camera:
    def take_photo(self):
        print("take photo")

class Phone:
    def make_call(self):
        print(f"Make call")

class Mobile(Camera,Phone):
    pass

m1 = Mobile()

m1.take_photo()
m1.make_call()