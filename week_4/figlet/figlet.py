import sys
from pyfiglet import Figlet
import random

def main():
    figlet = Figlet()
    fonts = figlet.getFonts()
    numberFonts = len(fonts)
    fontType = None
    f = ["-f", "--font"]

    if len(sys.argv) == 3 and sys.argv[1] in f and sys.argv[2] in fonts:
        fontType = str(sys.argv[2])
    elif len(sys.argv) != 1:
        sys.exit("Invalid usage")

    text = input("Input: ")
    if fontType == None:
        fontType = str(fonts[random.randint(0,numberFonts - 1)])
    figlet.setFont(font=fontType)
    print(figlet.renderText(text))

if __name__ == "__main__":
    main()

