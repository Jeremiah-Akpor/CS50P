import re
import sys


def main():
    print(validate(input("IPv4 Address: ")))


def validate(ip):
    """
    Validates an IPv4 address in the format X.X.X.X, where X is a number between 0 and 255.

    Args:
        ip (str): The IPv4 address to be validated.

    Returns:
        bool: True if the IP address is valid, False otherwise.
    """
    num = "(?:[0-9]|[1-9][0-9]|1[0-9]{2}|2[0-4][0-9]|25[0-5])"
    pattern = r"^" + num + r"\." + num + r"\." + num + r"\." + num + r"$"


    return (True if re.search(pattern,ip) else False)





if __name__ == "__main__":
    main()