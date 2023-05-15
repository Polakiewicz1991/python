class Animal:
    def __init__(self, name, age):
        self.name = name
        self.age = age

#w nawiasie klasa którą dziedziczymy
class Dog(Animal):
    def voice(self):
        print("How how")

class Cat(Animal):
    def getVoice(self):
        print("Meow meow")

class Wolf(Dog):
    def getVoice(self):
        print("Awooooooo")
        #super szuka w hierarhi diedziczenia funkcję
        super().voice()
        self.voice()


dog = Dog("Azor",10)
cat = Cat("Bursztyn",5)
wolf = Wolf("Gerald",50)

dog.voice()
print(dog.name)
print(dog.age)

cat.getVoice()
print(cat.name)
print(cat.age)

wolf.getVoice()
print(wolf.name)
print(wolf.age)