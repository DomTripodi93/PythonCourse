
def add_numbers(first_num, second_num):
    return first_num + second_num


number_sum = add_numbers(5, 6)

print("The value returned by add_numbers")
print(number_sum)

def add_number_list(number_list):
    return_num = 0
    for number in number_list:
        return_num += number
    return return_num


number_sum = add_number_list([5, 6, 7, 8])

print("\nThe value returned by add_number_list")
print(number_sum)
