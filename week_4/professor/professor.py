import random


def main():
    level = get_level()
    score = 0
    for _ in range(10):
        num_1 = generate_integer(level)
        num_2 = generate_integer(level)
        answer = num_1 + num_2
        trail = 0
        while trail != 3:
            try:
                user_answer = int(input(f"{num_1} + {num_2} ="))
                if user_answer != answer:
                    raise ValueError
                score += 1
                break
            except ValueError:
                print("EEE")
                trail += 1
        if trail == 3:
            print(f"{num_1} + {num_2} = {answer}")
    print(f"Your score is {score}")


def get_level():
    while True:
        try:
            num = int(input("Level: "))
            if num <= 0 or num > 3:
                raise ValueError
            return num
        except ValueError:
            pass


def generate_integer(level):
    if level == 2:
        return random.randint(10, 99)
    if level == 3:
        return random.randint(100, 999)
    return random.randint(0, 9)


if __name__ == "__main__":
    main()
