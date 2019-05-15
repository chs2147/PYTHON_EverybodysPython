picnicItems = {'apple':3,'banana':5}
picnicItems.setdefault('sandwich', 2)

print("Apple: " + str(picnicItems.get('apple',0)))
print("Egg: " + str(picnicItems.get('egg',0)))
print("Sandwich: " + str(picnicItems.get('sandwich',0)))
print(picnicItems)
