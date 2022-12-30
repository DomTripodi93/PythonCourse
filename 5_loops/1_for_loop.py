
my_number_list = [
    3,
    4,
    7,
    2,
    15
]

print("My whole list")
print(my_number_list)

my_square_list = []

for number in my_number_list:
    # print(number)
    my_square_list.append(number ** 2)

print("\nMy square list")
print(my_square_list)


my_filtered_list = []

my_filtered_list_simplified = {
    number for number in my_number_list if (number > 5)}
my_filtered_list_simplified = (
    number for number in my_number_list if (number > 5))
my_filtered_list_simplified = [
    number for number in my_number_list if (number > 5)]

for number in my_number_list:
    if (number > 5):
        my_filtered_list.append(number)


print("\nMy filtered list")
print(my_filtered_list)
print(my_filtered_list_simplified)


my_original_string = "this is some random sentence"

print("\nMy original sentence")
print(my_original_string)

my_string_list = my_original_string.split(" ")

my_capitalized_words_list = []

for string in my_string_list:
    my_capitalized_words_list.append(string[0].capitalize() + string[1:])

my_capitalized_sentence = str.join(" ", my_capitalized_words_list)

print("\nMy capitalized sentence")
print(my_capitalized_sentence)
