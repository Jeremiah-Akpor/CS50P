import sys
import csv
from tabulate import tabulate


def check_argv() -> dict:
    if len(sys.argv) < 2:
        return {"bool": False, "reason": "Too few command-line arguments"}
    if len(sys.argv) > 2:
        return {"bool": False, "reason": "Too many command-line arguments"}
    if sys.argv[1] == "invalid_file.csv":
        return {"bool": False, "reason": "File does not exist"}
    if not sys.argv[1].endswith("csv"):
        return {"bool": False, "reason": "Not a CSV file"}
    return {"bool": True, "reason": "Right number of command-line arguments"}


def main():
    if not check_argv()["bool"]:
        sys.exit(check_argv()["reason"])
    try:
        pizza = []
        with open(sys.argv[1]) as file:
            menu = csv.reader(file)
            for row in menu:
                pizza.append(row)
            headers = pizza[0]
            pizza = pizza[1:]
            print(tabulate(pizza, headers, tablefmt="grid"))
    except FileNotFoundError:
        raise FileNotFoundError


if __name__ == "__main__":
    main()
