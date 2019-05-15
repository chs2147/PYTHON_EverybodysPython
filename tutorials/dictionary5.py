allGuests = {'Alice': {'apples': 5, 'pretzels': 12},
             'Bob': {'ham sandwiches': 3, 'apples': 2},
             'Carol': {'cups': 3, 'apple pies': 1}}


def total_brought(guests, item):
    num = 0

    for k, v in guests.items():
        num += v.get(item,0)

    return num


print("Number of things brought: ")
print(" - Apples        : " + str(total_brought(allGuests,'apples')))
print(" - Cups          : " + str(total_brought(allGuests,'cups')))
print(" - Cakes         : " + str(total_brought(allGuests,'cakes')))
print(" - Ham Sandwiches: " + str(total_brought(allGuests,'ham sandwiches')))
print(" - Apple Pies    : " + str(total_brought(allGuests,'apple pies')))


