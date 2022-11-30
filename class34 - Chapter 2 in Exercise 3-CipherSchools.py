name, char= input("Enter name and character :").split(",")
print(f"length of your name is {len(name)}")
print(f"character count: {name.lower().count(char.lower())}")