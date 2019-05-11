import random

secretNumber = random.randint(1,20)
print("I am thinking of a number between 1 and 20.")

# Ask the player to guess 6 times
for guessChance in range(1,7):

    print("Take a guess:")
    guess = int(input())

    if guess > secretNumber:
        print("Your guess is too high.")
    elif guess < secretNumber:
        print("Your guess is too low.")
    else:
        break

if guess == secretNumber:
    print("Good job! You guessed my number in " + str(guessChance) + " guess(es)!")
else:
    print("Nope. The number I was thinking of was " + str(secretNumber))
