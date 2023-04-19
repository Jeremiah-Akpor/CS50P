def main():
    tweet = input("Input: ")
    tweet = shorten(tweet)
    print(f"Output: {tweet}")


def shorten(tweet: str) -> str:
    """convert twitter to twttr by removing the vowels

    Args:
        tweet (str): The input tweet.

    Returns:
        str: The tweet with vowels removed.
    """

    vowels = ["a", "e", "i", "o", "u"]
    twttr = []
    for t in tweet:
        if t.lower() in vowels:
            continue
        twttr.append(t)
    return "".join(twttr)


if __name__ == "__main__":
    main()
