import string


def main():
    plate = input("Plate: ")
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")


def is_valid(s):
    has_no_punctuation = not any(c in string.punctuation for c in s)

    # Check first character is a letter
    start_with_2_letter = s[:2].isalpha()

    # Check for numbers in the middle of the plate
    middle = int((len(s) - 1) / 2)
    no_middle_numbers = not s[middle].isdigit()

    # Check length
    correct_length = 2 <= len(s) <= 6

    # Check first number is not 0
    numbers = []
    for idx, c in enumerate(s):
        if c.isdigit():
            numbers.append(c)
            break
    if len(numbers) != 0:
        first_number = numbers[0] != "0"
    else:
        first_number = True

    return (
        start_with_2_letter
        and has_no_punctuation
        and correct_length
        and no_middle_numbers
        and first_number
    )


if __name__ == "__main__":
    main()
