import re
import sys


def main():
    print(parse(input("HTML: ")))


def parse(s):
    try:
        pattern = r"^<(?:\w|\s|\\\")*src=\"https?://(?:www\.)?youtube\.com/embed/([\w-]+)\".*$"
        match = re.search(pattern,s,re.IGNORECASE)
        return "https://youtu.be/" + match.group(1)
    except Exception:
        return None




if __name__ == "__main__":
    main()