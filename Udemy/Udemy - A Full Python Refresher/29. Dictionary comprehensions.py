users = [
    (0, "Bob", "Passowerd"),
    (1, "Kuba", "123RFV321"),
    (2, "Buba", "KlawiaturaiMysz"),
    (3, "Mati", "Barbie1"),
    (4, "xD", "mama"),
]

username_mapping = {user[1]: user for user in users}

print(username_mapping)
print("\n")
print(username_mapping["Bob"])

username_input = input("Enter username:")
username_password = input("Enter password:")

# _ bo nie nie obchodzi mnie index username = user[1] password = user[2]
_, username, password = username_mapping[username_input]

if  password == username_password:
    print("Acceds")