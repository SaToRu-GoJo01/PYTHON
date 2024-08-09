class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    
class chile(Person):
    pass

p1 = Person("Akash", 123)

p2 = chile("Akshit",12)

print(p1.name)
print(p2.name)