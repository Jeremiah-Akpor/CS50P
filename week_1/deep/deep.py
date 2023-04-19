answer = input("What is Answer to the Greatest Question of Life, the Universe, and Everything?" )
answer = answer.strip()
match answer.lower() :
    case "42" :
        print("Yes")
    case "forty-two" :
        print("Yes")
    case "forty two" :
        print("Yes")
    case _:
        print("No")

