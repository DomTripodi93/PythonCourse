
def add_number_list(*args):
    result_sum = 0
    for number in args:
        result_sum += number
    return result_sum


# list_of_numbers = [3, 4, 5, 1, 2, 3]

print(add_number_list(3, 4, 5, 1, 2, 3))
