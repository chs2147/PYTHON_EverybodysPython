import copy

def eggs(param1):
    param1.append("Bye")



spam = [0,1,2,3,4,5]
spam_text = "SPAM"
bread = copy.copy(spam)
cheese = spam
cheese_text = spam_text
cheese[1] = "Hello!"
spam_text = "CHEESE"

print(spam)
print(cheese)
print(spam_text)
print(cheese_text)

eggs(spam)
print(spam)
print(cheese)

print(bread)
