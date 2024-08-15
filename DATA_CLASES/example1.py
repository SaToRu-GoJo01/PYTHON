from dataclasses import dataclass
@dataclass
class data:
    Name: str
    Class: str
    Roll_no: int

student = data("Nikhil","Nothing",234)

print(student)