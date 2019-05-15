message = "It was a bright cold day in April, and the clocks were striking thirteeen."
word_count = {}

for character in message:
    word_count.setdefault(character,0)
    word_count[character] += 1

for itm in word_count.items():
    print(itm)

