import random

Alphabet_1 = random.choice('abcdefghijklmnopqrstuvwxyz')

for i in range(4):
    x = input("Enter an alphabet between a to z: ")

    if x > Alphabet_1:
        print("Your alphabet is too high")

    elif x < Alphabet_1:
        print("Your alphabet is too low")

    else:
        print("You guessed it right!")
        break

print("The alphabet was:", Alphabet_1)