friend = [
    {"name": "Kuba", "age" : 24},
    {"name": "Buba", "age": 26},
    {"name": "Luba", "age": 29},
]
print(friend[1]["name"])

students_attendance = \
    {"Kuba" : 96,
     "Buba":85,
     "Luba":77}

for student in students_attendance:
    print(f"{student}: {students_attendance[student]}")


print("\n\n\n\n")

for student, attendance in students_attendance.items():
    print(f"{student}: {attendance}")

if "Bob" in students_attendance:
    print(f"Bob: {students_attendance['Bob']}")
else:
    print("Bob is not a student")

students_values = students_attendance.values()

print(sum(students_values)/len(students_values))