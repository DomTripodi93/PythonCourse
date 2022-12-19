
def maybe_display_sum(display_sum, /, *args):
    result_sum = 0
    for number in args:
        result_sum += number
    if (display_sum):
        print(result_sum)
    return result_sum


print("Calling maybe_display_sum with display_sum = False")
returned_sum = maybe_display_sum(False, 3, 4)
print(returned_sum)


def function_with_callback(run_callback, callback, callback_args):
    if run_callback:
        print("\nRunning callback")
        # callback()
        return callback(*callback_args)
    else:
        print("\nDidn't run callback")
        return 0


print("\nCalling function_with_callback on maybe_display_sum with run_callback = True")
# returned_sum = function_with_callback(True, maybe_display_sum(True, 3, 4, 5, 6, 7))
returned_sum = function_with_callback(True, maybe_display_sum, [True, 3, 4, 5, 6, 7])


print("\nThe value of returned_sum when run_callback = True")
print(returned_sum)



print("\nCalling function_with_callback on maybe_display_sum with run_callback = False")
returned_sum = function_with_callback(False, maybe_display_sum, [True, 3, 4, 5, 6, 7])


print("\nThe value of returned_sum when run_callback = False")
print(returned_sum)
