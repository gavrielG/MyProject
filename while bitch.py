import random
number=random.randint(1,9)
guess=int(input("guess a number:"))

while guess!=number:
    if guess<number:
        print("your number is lower try again")
        guess = int(input("guess a number:"))
    else:
        print("you need to guess higher try again")
        guess = int(input("guess a number:"))
print("you guess the number correct!")





