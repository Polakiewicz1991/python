studentStandard = {"name": "Paweł", "grades": (98,99,95,78,93)}

def average(sequence):
    return sum(sequence) / len(sequence)

print(average(studentStandard["grades"]))


class Student:
    def __init__(self,name):
        # self.name = "Paweł"
        self.name = name
        self.grades = (98,99,95,78,93)
    def __str__(self):
        return (f"Mam na imie {self.name}")

    def average_grades(self):
        return sum(self.grades) / len(self.grades)

student1 = Student("Bob")
student2 = Student("Kuba")
print(student1)
print(student1.name)
print(student1.grades)
print(student1.average_grades())
print("\n")
print(Student.average_grades(student1)) #Wywołamy funkcję klasy Student dla obieku student
print(student2)