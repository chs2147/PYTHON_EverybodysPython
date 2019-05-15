allGuests = {'Alice': {'apples':5, 'pretzels':12},
             'Bob': {'ham sandwiches':3, 'apples':2},
             'Carol': {'cups':3, 'apple pies':1}}

def totalBrought(guests, item):
    num = 0

    for k,v in guests.items():
        num += v.get(item,0)

    return num

print("Number of things brought: ")
print(" - Apples        : " + str(totalBrought(allGuests,'apples')))
print(" - Cups          : " + str(totalBrought(allGuests,'cups')))
print(" - Cakes         : " + str(totalBrought(allGuests,'cakes')))
print(" - Ham Sandwiches: " + str(totalBrought(allGuests,'ham sandwiches')))
print(" - Apple Pies    : " + str(totalBrought(allGuests,'apple pies')))


