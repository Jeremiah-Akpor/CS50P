user_input = input("input: ")
split_input = user_input.split()


def convert_emoji(string):
    if string == ":)":
        return "🙂"
    if string == ":(":
        return "🙁"
    return string


output = [convert_emoji(str) for str in split_input]
print(" ".join(output))
