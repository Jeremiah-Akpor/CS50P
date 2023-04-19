import requests
import sys


def price():
    while True:
        try:
            if len(sys.argv) == 1:
                sys.exit("Missing command-line argument")
            bitcoin = requests.get("https://api.coindesk.com/v1/bpi/currentprice.json")
            result = bitcoin.json()
            rate = float(result["bpi"]["USD"]["rate_float"])
            return float(sys.argv[1]) * rate
        except (requests.RequestException):
            pass
        except ValueError:
            sys.exit("Command-line argument is not a number")


def main():
    amount = price()
    print(f"${amount:,.4f}")

if __name__ == "__main__":
    main()
