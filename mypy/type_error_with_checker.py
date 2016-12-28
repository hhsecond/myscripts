import random
from typing import Union, Any, List, cast

def compare(guess: int, secret: int) -> bool:
    if guess == secret:
        print("you win")
        return True
    else:
        print("try again loser!")
        return False

if __name__ == "__main__":
    secret = random.choice([3, 4])
    print("secret number is {}".format(secret))

    game_over = False
    while not game_over:
        guess = int(input("please input your number"))
        print("Your guess is {}".format(guess))
        game_over = compare(guess, secret)
