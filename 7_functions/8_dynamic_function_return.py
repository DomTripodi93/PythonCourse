
def function_create():
    def maybe_display_sum(display_sum, /, *args):
        result_sum = 0
        for number in args:
            result_sum += number
        if (display_sum):
            print(result_sum)
        return result_sum
    return maybe_display_sum


returned_function = function_create()
print("The function that was returned")
print(returned_function)


print("\nCalling returned_function with display_sum = False")
returned_sum = returned_function(False, 3, 4)
print(returned_sum)


print("\nCalling function_creator's result with display_sum = False")
returned_sum = function_create()(False, 3, 4)
print(returned_sum)
