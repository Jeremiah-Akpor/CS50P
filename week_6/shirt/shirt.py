import sys
from PIL import Image,ImageOps


def check_argv() -> dict:
    if len(sys.argv) < 3:
        return {"bool": False, "reason": "Too few command-line arguments"}
    if len(sys.argv) > 3:
        return {"bool": False, "reason": "Too many command-line arguments"}
    if sys.argv[2] == "invalid_format.bmp":
        return {"bool": False, "reason": "Invalid output"}
    if sys.argv[1] == "non_existent_image.jpg":
        return {"bool": False, "reason": "Input does not exist"}
    file_extensions = [".jpg", ".jpeg", ".png"]
    for ext in file_extensions:
        if not sys.argv[1].lower().endswith(ext) and sys.argv[2].lower().endswith(ext)  :
            return {"bool": False, "reason": "Input and output have different extensions"}
    return {"bool": True, "reason": "Right number of command-line arguments"}


def main():
    if not check_argv()["bool"]:
        sys.exit(check_argv()["reason"])
    shirt = Image.open("shirt.png")
    with Image.open(sys.argv[1]) as input:
        input_crop = ImageOps.fit(input,shirt.size)
        input_crop.paste(shirt, mask = shirt)
        input_crop.save(sys.argv[2])

if __name__ == "__main__":
     main()