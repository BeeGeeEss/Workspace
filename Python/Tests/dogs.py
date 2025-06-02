class Dog:
    species = "Canis familiaris"

    def __init__(self, name, age):
        self.name = name
        self.age = age

    # Instance method
    #def description(self):
        #return f"{self.name} is {self.age} years old"
    def __str__(self):
        return f"{self.name} is {self.age} years old"

    # Another instance method
    def speak(self, sound):
       return f"{self.name} barks: {sound}"  

class JackRussellTerrier(Dog):
    def speak(self, sound="Arf"):
        return super().speak(sound)

class Dachshund(Dog):
    pass

class Bulldog(Dog):
    pass     

miles = JackRussellTerrier("Miles", 4)
buddy =  Dachshund("Buddy", 9)

print(miles.speak)
print(miles.speak("Woof Woof"))
print(miles)
print(type(miles))
print(isinstance(miles, Dog))
print(isinstance(miles, JackRussellTerrier))
