import random;

def guess(x):
    random_num = random.randint(1, x)
    guess = 0
    while guess != random_num:
        guess = int(input(f"Guess a number between 1 and {x}: "))
        if (guess > random_num):
            print("Too high")
        elif (guess < random_num):
            print("too low")
    
    print(f"You have guessed correctly. The correct number was {random_num}")

guess(10)