import emoji

def getUserInput(prompt: str) -> str:
    userInput = input(prompt)
    userInput = userInput.split()
    for idx,word in enumerate(userInput):
        if word[0] == ":":
            userInput[idx] = emoji.emojize(word)
    return " ".join(userInput)


def main():
    print(getUserInput("Input: "))

if __name__ == "__main__":
    main()