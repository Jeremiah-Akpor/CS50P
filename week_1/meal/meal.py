def main():
    time = input("What time is it? ")
    converted_time = convert(time)
    if converted_time >= 7.0 and converted_time <= 8.0:
        print("breakfast time")
    if converted_time >= 12.0 and converted_time <= 13.0:
        print("lunch time")
    if converted_time >= 18.0 and converted_time <= 19.0:
        print("dinner time")

def convert(time):
    hour, minute = time.split(":")
    return float(hour) + (float(minute)  / 60)


if __name__ == "__main__":
    main()

