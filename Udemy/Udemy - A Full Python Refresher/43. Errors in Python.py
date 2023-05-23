def divide(divided, divisor):
    if divisor == 0:
        raise ZeroDivisionError("Kurdebele Divisor cannot be 0")

    return divided / divisor

students = [{"name": "Kuba", "grades": [95,22]},
            {"name": "Luba", "grades": []},
            {"name": "Huba", "grades": [96,77,87]},]

try:
    for student in students:
        name = student["name"]
        grades = student["grades"]
        print(grades)
        average = divide(sum(grades),len(grades))
        print(f"{name} Average: {average}")
except ZeroDivisionError as e:
    # print(e)
    print(f"{name} has no grades")
    print("There are no grades yet")
else:
    print("All students ware calculated")
    print(f"Average: {average}")
finally:
    print("Thank you")
