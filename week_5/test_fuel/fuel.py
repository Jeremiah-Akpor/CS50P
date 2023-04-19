def main():
    while True:
        try:
            level = input("Fraction: ")
            percentage = convert(level)
            x = gauge(percentage)
            break
        except (ValueError, ZeroDivisionError):
            pass
    print(x)


def convert(fraction):
    x, y = map(int, fraction.split("/"))
    if y == 0:
        raise ZeroDivisionError
    if x > y:
        raise ValueError
    return round((x / y) * 100)


def gauge(percentage):
    if percentage <= 1:
        return "E"
    if percentage >= 99:
        return "F"
    return f"{percentage}%"


if __name__ == "__main__":
    main()
