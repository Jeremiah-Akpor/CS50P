def main():
    camelcase = input("camelCase: ")
    print(convert_to_snake_case(camelcase))

def convert_to_snake_case(variable: str):
    snake_case = variable.lower()
    count = 0                           # it counts the number of underscore ("_") added to the string
    for idx, v in enumerate(variable):
        if v.isupper() and idx != 0:
            snake_case = snake_case[:idx+count] + "_" + snake_case[idx+count:]
            count += 1
    return snake_case

if __name__ == "__main__":
    main()