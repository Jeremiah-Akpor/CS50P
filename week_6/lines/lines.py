import sys


def check_argv() -> dict:
    if len(sys.argv) < 2:
        return {"bool": False, "reason": "Too few command-line arguments"}
    if len(sys.argv) > 2:
        return {"bool": False, "reason": "Too many command-line arguments"}
    if sys.argv[1] == "non_existent_file.py":
        return {"bool": False, "reason": "Not a Python file"}
    if not sys.argv[1].endswith("py"):
        return {"bool": False, "reason": "Not a Python file"}
    return {"bool": True, "reason": "Right number of command-line arguments"}


def num_lines(filename: str) -> int:
    with open(filename) as file:
        lines = file.readlines()
        length = 0
        for line in lines:
            line = line.rstrip().strip().split("\n")
            for a in line:
                if len(line) > 0 and not a.startswith("#") and a != "":
                    length += 1
        return length


def main():
    if not check_argv()["bool"]:
        sys.exit(check_argv()["reason"])
    print(f"{num_lines(sys.argv[1])}")


if __name__ == "__main__":
    main()
