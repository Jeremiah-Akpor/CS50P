months = [
    "January",
    "February",
    "March",
    "April",
    "May",
    "June",
    "July",
    "August",
    "September",
    "October",
    "November",
    "December",
]


def convertDate(prompt):
    while True:
        try:
            date = input(prompt)
            if date == "" or ("," not in date and "/" not in date):
                continue
            if "/" in date and date[0].isalpha():
                continue
            date = date.replace("/", " ").replace(",", " ")
            month, day, year = date.split()
            if not (day.isdigit() and year.isdigit()):
                continue
            day = int(day)
            if not 1 <= day <= 31:
                continue
            month = int(months.index(month) + 1) if not month.isdigit() else int(month)
            if int(month) > 12:
                continue
            return f"{year}-{month:02}-{day:02}"
        except EOFError:
            continue


def main():
    date = convertDate("Date: ")
    print(date)


main()
