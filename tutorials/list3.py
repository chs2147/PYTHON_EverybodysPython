myPets = ["dog","cat","tiger"]

print("Enter a pet name: ")
name = input()

if name not in myPets:
    print("Your pet is not in my list.")
else:
    print(name + " is my pet.")
