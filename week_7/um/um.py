import re
import sys


def main():
    print(count(input("Text: ")))


def count(s):
    pattern = r"\bum\b"
    # Use re.findall() to find all occurrences of the character in the input string
    matches = re.findall(pattern, s , re.IGNORECASE)
    print(matches)
    # Get the count of occurrences using len()
    return len(matches)

if __name__ == "__main__":
    main()