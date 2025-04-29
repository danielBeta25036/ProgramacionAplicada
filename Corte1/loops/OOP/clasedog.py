class Dog:
    species = "Canis familiaris"

    def __init__(self, name, age):
        self.name = name
        self.age = age

    
    def description(self, name, age):
        return f"{self.name} is {self.age} years old"

    # Another instance method
    def speak(self, sound):
        return f"{self.name} says {sound}"

miles = Dog("Miles", 4)



miles.description("miles", 4)


#miles.speak("Woof Woof")


#miles.speak("Bow Wow")
