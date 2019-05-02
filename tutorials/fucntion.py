#function example


def hello():
    print("Howdy!")
    print("Howdy!!!")
    print("Hello there.")


def hello2(name):
    print("My name is: " + name)


def getAnswer(answerNum):
    if answerNum == 1:
        return "Number One"
    elif answerNum == 2:
        return "Number Two"
    elif answerNum == 3:
        return "Number 3"
    else:
        return "Bigger than 3"


hello()
hello()
hello()

hello2("CHEN")
hello2("JENNY")

print(getAnswer(1))
print(getAnswer(3))
print(getAnswer(6))

