from abc import ABC, abstractmethod

class website(ABC):
    def show_photo(self):
        print("Photos are shown")

    def show_files(self):
        print("Files are shown")

    @abstractmethod
    def responsive(self):
        pass

class Laptop(website):
    def responsive(self):
        print("Made responsive for laptop")

class Mobile(website):
    def responsive(self):
        print("Made responsive for Mobile.")


l1 = Laptop()
l1.responsive()
l1.show_files()
l1.show_photo()
print()
m1 = Mobile()
m1.responsive()
m1.show_photo()
m1.show_files()


from abc import ABC,abstractmethod

class Shape(ABC):
    def __init__(self,length,width):
        self.length = length
        self.width = width

    @abstractmethod
    def are(self):
        pass
