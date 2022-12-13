# some_int = 2
# some_int = 7
# some_int = 5
# some_int = False
some_int = "words"

match some_int:
    case 2:
        print("value is 2")
    case 7:
        print("value is 7")
    case False:
        print("value is False")
    case "words":
        print("value is words")
    case other:
        print("not an expected match")
