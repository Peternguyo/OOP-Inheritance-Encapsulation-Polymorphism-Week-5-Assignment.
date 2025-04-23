
#creating base class.i've created a general Animal class with a common method move()
class Animal:
    def move(self):
        print("Animal moves.")


#create subclasses with the specialized move() methods
class Dog(Animal):
    def move(self):
        print("Running on four legs.")

class Snake(Animal):
    def move(self):
        print("Slithering on the ground.")

class Bird(Animal):
    def move(self):
        print("Flying through the air.")

#demonstrating polymorphism-create a list of different animal objects and call their move() method. 
animals = [Dog(), Snake(), Bird()]

for animal in animals:
    animal.move()


 #output:   
""" Running on four legs.
Slithering on the ground.
Flying through the air """ 
