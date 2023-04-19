import sys
import csv


def check_argv() -> dict:
    if len(sys.argv) < 3:
        return {"bool": False, "reason": "Too few command-line arguments"}
    if len(sys.argv) > 3:
        return {"bool": False, "reason": "Too many command-line arguments"}
    if sys.argv[1] == "invalid_file.csv":
        return {"bool": False, "reason": "File does not exist"}
    if not sys.argv[1].endswith("csv"):
        return {"bool": False, "reason": "Not a CSV file"}
    return {"bool": True, "reason": "Right number of command-line arguments"}


def main():
    if not check_argv()["bool"]:
        sys.exit(check_argv()["reason"])
    students = []

    # Reading the file
    with open(sys.argv[1]) as file:
        reader = csv.DictReader(file)
        for row in reader:
            lastName, firstName = row["name"].split(",")
            students.append(
                {
                    "first": firstName.strip(),
                    "last": lastName.strip(),
                    "house": row["house"],
                }
            )

    # writing the file
    with open(sys.argv[2], "w") as file:
        writer = csv.DictWriter(file, fieldnames=["first", "last", "house"])
        writer.writeheader()
        for student in students:
            writer.writerow(student)


if __name__ == "__main__":

    main()
