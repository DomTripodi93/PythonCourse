
def partially_edited_function(show_message, /, **kwargs):
    print(kwargs)
    if (show_message):
        print(kwargs["message"])
    if ("alt_message" in kwargs):
        print(kwargs["alt_message"])
    else:
        print("Some default message")


print("\nCalling partially_edited_function with show_message = True")
partially_edited_function(True, message="something")

print("\nCalling partially_edited_function with show_message = False")
partially_edited_function(False, message="something")

print("\nCalling partially_edited_function with an alt_message and show_message = False")
partially_edited_function(False, message="something",
                          alt_message="An additional keyword was added")


def maybe_display_sum(display_sum, /, *args):
    result_sum = 0
    for number in args:
        result_sum += number
    if (display_sum):
        print(result_sum)
    return result_sum


print("\nCalling maybe_display_sum with display_sum = True")
returned_sum = maybe_display_sum(True, 3, 4, 5, 6, 7)
print(returned_sum)

print("\nCalling maybe_display_sum with display_sum = False")
returned_sum = maybe_display_sum(False, 3, 4)
print(returned_sum)
