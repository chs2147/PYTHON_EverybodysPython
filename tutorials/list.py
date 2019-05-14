spam = ["cat","dog","rat","elephant"]

# index
print("* get value with index *")
print(spam[0])
print(spam[3])
print()

# negative index
print ("* get value with negative index *")
print(spam[-1])
print(spam[-3])
print()

# slices
print("* get values with slices *")
print(spam[0:4])
print(spam[1:3])
print(spam[0:-2])
print()

# length
print("* length of list *")
print(len(spam))
print()

# changing value on list
spam[1] = "tiger"
spam[3] = spam[1]
print(spam[0:4])
print()

# finding value in a list with the index() method
print("* finding value on list with index method *")
print(spam.index("rat"))
print()

# list on list
tray = [["banana","apple"],[10,20,30,40]]

print("* list on list *")
print(tray[0][1])
print(tray[1][2])
print()

#length
print(len(tray))

# list concatenation and replication
bacon = ["A","B","C"]

print(spam+bacon)
print(bacon*3)

bacon = bacon + spam
print(bacon)

# removing value from list with del statements
del spam[2]
print(spam)

del spam[2]
print(spam)

# adding values to lists with the append and insert methods
spam.append("duck")
print("* append *")
print(spam)
print()

spam.insert(2, "chicken")
print("* insert *")
print(spam)
print()

# removing values from lists with remove method
spam.remove("tiger")

print("* remove *")
print(spam)
print()

# sorting the values in a list with the sort method
numberList = [1,2,0,-1,5,3.14,-7,10,4,3]
wordList = ["zoro","Coba","chem","fire","avast","Avast",]

numberList.sort()
wordList.sort()

print("* sort by ascending *")
print(numberList)
print(wordList)
print()

