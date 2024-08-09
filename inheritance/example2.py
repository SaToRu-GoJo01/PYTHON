class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

class child(Person):
    def __init__(self, name):
        self.name = name
        Person.__init__(self, name,100)


p2 = Person("Akshit",100)
p1 = child("Hello")

print(p1.name)