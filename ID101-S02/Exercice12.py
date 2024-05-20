C = int(input("Donner un nombre :"))
match C:
    case 1: print("a")
    case 2: print("b")
    case 3: print("c")
    case 4,5: print("d")
    case _: print("?")