#Creating my own iterator for a class object 

class myClass:
    def __iter__(self):
        self.a = 1
        return self
    
    def __next__(self):
        x = self.a
        self.a += 1
        return x


obj = myClass()
my_iterator = iter(obj)

print(next(my_iterator))
print(next(my_iterator))
print(next(my_iterator))
print(next(my_iterator))

#stopin iterations after certain number of __next__

class second:
    def __iter__(self):
        self.a = 1
        return self
    
    def __next__(self):
        if self.a < 20:
            x = self.a
            self.a += 1
            return x
        else:
            raise StopIteration
        
obj2 = second()
my_iterator2 = iter(obj2)
for i in my_iterator2:
    print(i)
# print(next(my_iterator2)) it will raise error type StopIteration