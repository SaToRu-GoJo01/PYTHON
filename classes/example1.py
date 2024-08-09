class test:
    def __init__(self,name) -> None:
        self.name = name

    def __str__(self) -> str:
        return self.name
    
t1 = test("Akash")
print(t1)