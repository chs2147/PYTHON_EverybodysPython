"""

This is the example program for string operations

"""


print("Hello there!\nHow are you?\nI\'m doing fine.")
print()
print(r"Hello there!\nHow are you?\nI\'m doing fine.")
print()

my_letter = """Dear Alice.

Eve's cat has been arrested for catnapping.

Sincerely,
Bob"""

print(my_letter)

spam = "Hello World!"

spam = spam.upper()
print(spam)

spam = spam.lower()
print(spam)

# join, split

str1 = ','.join(['apple','banana','orange'])
str2 = ' vs. '.join(['Ken','Ryu','Chunli'])
str3 = ' '.join(['My','name','is','Leslie'])

print(str1)
print(str2)
print(str3)

str4 = str2.split(' vs. ')
print(str4)

my_letter = my_letter.split('\n')
print(my_letter)

# Justifying Text with rjust(), ljust(), center()

print('Hello'.rjust(11))
print('Hello'.rjust(11, '*'))
print('Hello'.center(11, '*'))

# Removing Whitespace with strip(), lstrip(), rstrip()

spam = "    ABC is DEF      "

print("\'" + spam + "\'")
print("\'" + spam.lstrip() + "\'")
print("\'" + spam.rstrip() + "\'")
print("\'" + spam.strip() + "\'")
