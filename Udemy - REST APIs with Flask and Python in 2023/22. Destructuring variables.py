students_attendance = \
    {"Kuba":    96,
     "Buba":    85,
     "Luba":    77}

for student in students_attendance.items(): #wzraca krotkę
    print(student)

for student, attendence in students_attendance.items(): #wzraca krotkę
    print(student,attendence)

people = \
    [("Kuba",    96, "Mechanik"),
     ("Buba",    85, "Elektryk"),
     ("Luba",    77, "Konstruktor")]

# for person, age, profession in people:
for person in people:
    print(person)
    print(person[0],person[1],person[2])

person = ("Kuba",    96, "Mechanik")
name, _ , profession = person

head, *taill = [1,2,3,4,5]
print(head)
print(taill)