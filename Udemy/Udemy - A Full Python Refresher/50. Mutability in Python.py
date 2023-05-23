from typing import List, Optional
a = []
b = a
# b = []

a.append(35)

print(id(a))
print(id(b))

print(a)
print(b)

class Student:
    #def __init__(self,name: str, grades: List[int] = []): # tak nie można bo wszystkie klasy będą odwoływać się to tej samej defaultowej tabeli []
    def __init__(self, name: str, grades: List[int] = None):
        self.name = name
        self.grades = grades or []

    def __str__(self):
        return (f"Mam na imie {self.name}")

    def take_exam(self,result, int):
        self.grades.append(result)

    def average_grades(self):
        return sum(self.grades) / len(self.grades)