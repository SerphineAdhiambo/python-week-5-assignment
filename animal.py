# Animal base class
class Animal:
    def move(self):
        pass

# Dog class inherits from Animal
class Dog(Animal):
    def move(self):
        print("The dog is running! 🐕")

# Cat class inherits from Animal
class Cat(Animal):
    def move(self):
        print("The cat is walking! 🐈")

# Bird class inherits from Animal
class Bird(Animal):
    def move(self):
        print("The bird is flying! 🕊️")
# Creating instances of Dog, Cat, and Bird
dog = Dog()
cat = Cat()
bird = Bird()

# Calling the move() method, which behaves differently for each animal
dog.move()   # Outputs: The dog is running! 🐕
cat.move()   # Outputs: The cat is walking! 🐈
bird.move()  # Outputs: The bird is flying! 🕊️
