#! python3
# bullet point adder - Adds Wikipedia bullet points to the start
# of each line of text on the clipboard


import pyperclip

text = pyperclip.paste()

print("pasted: \n" + text)

# Separate lines and add stars.
lines = text.split('\n')

for i in range(len(lines)):
    lines[i] = '* ' + lines[i]

text = '\n'.join(lines)
pyperclip.copy(text)


