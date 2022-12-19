
def add_number_args(*args):
    return_num = 0
    for number in args:
        return_num += number
    return return_num


number_sum = add_number_args(5, 6, 7, 8, 9, 10)

print("\nThe value returned by add_number_args")
print(number_sum)


def commonly_edited_function(**kwargs):
    print(kwargs)
    # print(kwargs["test"])
    # if (kwargs["show_test"]):
    if ("show_message" in kwargs and kwargs["show_message"]):
        print(kwargs["message"])
    else:
        print("Some default message")


# print("\nCalling commonly_edited_function: commonly_edited_function(test=\"something\")")
# commonly_edited_function(test="something")

print("\nCalling commonly_edited_function with show_message = True")
commonly_edited_function(message="something", show_message=True)

print("\nCalling commonly_edited_function with show_message = False")
commonly_edited_function(message="something", show_message=False)

print("\nCalling commonly_edited_function without show_message")
commonly_edited_function(message="something")
