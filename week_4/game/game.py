from random import randint


def get_user_input(prompt):
    while True:
        try:
            num = int(input(prompt))
            if num <= 0:
                raise ValueError
            return num
        except ValueError:
            pass


def main():
    n = get_user_input("Level: ")
    level = randint(1, n )
    guess = -1
    while level != guess:
        guess = get_user_input("Guess: ")
        if guess == level :
            quit("Just right!")
        if guess > level :
            print("Too large!")
            continue
        print("Too small!")

if __name__ == "__main__":
    main()
