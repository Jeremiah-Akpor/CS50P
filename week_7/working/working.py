import re
import sys


def main():
    print(convert(input("Hours: ")))


def convert(s):
    pattern = r"^(0?[0-9]|1[0-2])(?:\:([0-5]?[0-9]?))?\s(AM|PM)\s?to\s(0?[0-9]|1[0-2])(?:\:([0-5]?[0-9]?))?\s(AM|PM)\s?$"
    match = re.search(pattern, s, re.IGNORECASE)

    def get_hour_and_minutes(hour, minutes, am_or_pm):
        if hour + 12 == 24 and am_or_pm == "AM":
            return "00", minutes
        elif hour + 12 != 24 and am_or_pm == "PM":
            return str(hour + 12), minutes
        else:
            return str(hour).zfill(2), minutes

    try:
        hour_1 = int(match.group(1))
        minutes_1 = "00" if match.group(2) is None or match.group(2) == 'None' else match.group(2)
        am_or_pm_1 = match.group(3)
        hour_1, minutes_1 = get_hour_and_minutes(hour_1, minutes_1, am_or_pm_1)

        hour_2 = int(match.group(4))
        minutes_2 = "00" if match.group(5) is None or match.group(5) == 'None' else match.group(5)
        am_or_pm_2 = match.group(6)
        hour_2, minutes_2 = get_hour_and_minutes(hour_2, minutes_2, am_or_pm_2)

        return f"{hour_1}:{minutes_1} to {hour_2}:{minutes_2}"
    except AttributeError:
        raise ValueError("Invalid input format")




if __name__ == "__main__":
    main()