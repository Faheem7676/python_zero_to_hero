# Base class (Parent class)
class Animal:
    def __init__(self, name):
        self.name = name

    def speak(self):
        return f"{self.name} makes a sound."

# Derived class (Child class)
class Dog(Animal):
    def __init__(self, name, breed):
        super().__init__(name)  # Call the parent class constructor
        self.breed = breed

    def speak(self):
        return f"{self.name}, a {self.breed}, says 'Woof!'"

# Another Derived class
class Cat(Animal):
    def __init__(self, name, color):
        super().__init__(name)
        self.color = color

    def speak(self):
        return f"{self.name}, a {self.color} cat, says 'Meow!'"

# Using the classes
dog = Dog("Buddy", "Golden Retriever")
cat = Cat("Whiskers", "black")

print(dog.speak())  # Output: Buddy, a Golden Retriever, says 'Woof!'
print(cat.speak())  # Output: Whiskers, a black cat, says 'Meow!'