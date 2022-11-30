winning_number= 68
user_input= input("Guess any number b/w 1 & 100\n")
user_input= int(user_input)
if user_input==winning_number:
    print("YOU WIN!")
else:
    if user_input < winning_number:
        print("too low")
    else:
        print("too high")