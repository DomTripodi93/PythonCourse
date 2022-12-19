
def add_number_list(number_list):
    return_num = 0
    for number in number_list:
        return_num += number
    return return_num


number_sum = add_number_list([5, 6, 7, 8])

print("\nThe value returned by add_number_list")
print(number_sum)


def add_number_args(*args):
    return_num = 0
    for number in args:
        return_num += number
    return return_num


number_sum = add_number_args(5, 6, 7, 8, 9, 10)

print("\nThe value returned by add_number_args")
print(number_sum)
