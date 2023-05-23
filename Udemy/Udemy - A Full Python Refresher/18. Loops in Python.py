number = 7

user_input = input("Would you like to play? (y/n):")

#<editor-fold> desc = "1st"
while user_input != 'n':
    user_number = int(input("Guess our number: "))
    if user_number == number:
        print("Correct")
    elif abs(number- user_number) == 1:
    # elif (number - user_number) in (1, -1):
        print("You were off by one.")
    else:
        print("Not correct")
    user_input = input("Would you like to play again? (y/n):")
# </editor-fold>

while True:
    if user_input == 'n':
        break
    user_number = int(input("Guess our number: "))
    if user_number == number:
        print("Correct")
    elif abs(number- user_number) == 1:
    # elif (number - user_number) in (1, -1):
        print("You were off by one.")
    else:
        print("Not correct")

    user_input = input("Wounld you like to play again? (y/n):")


friends = {"Kuba", "Buba", "Luba"}
for friend in friends:
    print(f"{friend} is friend")