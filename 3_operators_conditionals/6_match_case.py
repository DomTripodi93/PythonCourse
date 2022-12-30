import datetime

# my_generic_variable = datetime.datetime(2023, 6, 15).strftime("%Y/%m/%d")
my_generic_variable = "random string"

match my_generic_variable:
    case 5:
        print("The value is 5")
    case "random string":
        print("The value is \"random string\"")
    case False:
        print("The value is False")
    # case datetime.datetime(2023, 6, 15):
    case "2023/06/15":
        print("The value is June 15 2023")
    case other:
        print("Our variable had no match")
