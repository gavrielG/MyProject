import random
number=random.randint(1,100)
guess=int(input("guess a number:"))
tries=0

while number!=guess:
    if guess<number:
        print("your number is higher try again")
        guess = int(input("guess a number:"))
        tries+=1
    else:
        print("you need to guess lower try again")
        guess = int(input("guess a number:"))
        tries+=1
print(f"you guess the number right it took you {tries} tries")

