birthdays = {'Alice':'Apr 1', 'Bob':'Dec 12', 'Carol':'Mar 4'}
input_log = {}
cnt = 0

while True:
    print("Enter a name: (blank to quit)")
    name = input()

    if name == "":
        break

    if name in birthdays.keys():
        print(birthdays[name] + " is the birthday of " + name)
    else:
        print("I do not have birthday information of " + name)

        print("What is their birthday?")
        bday = input()
        birthdays[name] = bday
        print("Birthday database updated.")

    cnt += 1
    input_log[cnt] = name

print(birthdays)
print(input_log)

print("* dict values *")
for i in birthdays.values():
    print(i)

print("* dict keys *")
for i in birthdays.keys():
    print(i)

print("* dict items *")
for i in birthdays.items():
    print(i)

print("* dict keys and values *")
for k,v in birthdays.items():
    print("K: " + k)
    print("V: " + v)
