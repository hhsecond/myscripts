import random

def compare(guess, secret):
    if guess == secret:
        print("you win")
        return True
    else:
        print("try again loser!")
        return False

if __name__ == "__main__":
    secret = random.randint(1, 101)
    print("secret number is {}".format(secret))

    game_over = False
    while not game_over:
        guess = input("please input your number")
        print("Your guess is {}".format(guess))
        game_over = compare(guess, secret)