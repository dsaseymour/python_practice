class Dog:
    species = "Canis familiaris"
    def __init__(self, name, age,coat_color):
        self.name = name
        self.age = age
        self.coat_color=coat_color
    # Instance method
    def description(self):
        return f"{self.name} is {self.age} years old"
    # Another instance method
    def speak(self, sound):
        return f"{self.name} says {sound}"
