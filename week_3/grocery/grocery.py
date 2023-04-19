grocery_list = {}


def main():
    while True:
        try:
            grocery = input().upper()
            if grocery == "":
                raise EOFError
            if grocery in grocery_list:
                grocery_list[grocery] += 1
            else:
                grocery_list[grocery] = 1
        except EOFError:
            for key in sorted(grocery_list.keys()):
                print(f"{grocery_list[key]} {key}")
            break
        else:
            continue


main()
