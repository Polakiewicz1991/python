import random
class Student:
    def __init__(self, name,surname,age,city):
        self.name = name
        self.surname = surname
        self.age = age
        self.city = city
        self.schoolName = None
        self.fieldOfStudy = None


    def printInfo(self):
        print(self.name, self.surname, self.age,self.city,self.schoolName,self.fieldOfStudy)


class School:
    def __init__(self, name, city):
        self.name = name
        self.city = city
        self.studentsList = []
        self.fieldsOfStudy = ["IT","Math","Robotics"]


    def addStudent(self,student):
        if isinstance(student, Student):
            self.studentsList.append(student)
            student.schoolName = self.name
            student.fieldOfStudy = random.choice(self.fieldsOfStudy)


    def printSchoolInfo(self):
        print("Szkoła ",self.name," w ", self.city)
        print("Student:")
        for el in self.studentsList:
            el.printInfo()

student1 = Student("Kasia","Lis", 20, "Krk")
student1.schoolName = "Kupa"
student2 = Student("Asia","Wilk", 21, "Krk")
student2.schoolName = "Lupa"
student3 = "Kupa"

student1.printInfo()
student2.printInfo()

school = School("PK", "Piwniczna")
school.addStudent(student1)
school.addStudent(student2)
school.addStudent(student3)

school.printSchoolInfo()