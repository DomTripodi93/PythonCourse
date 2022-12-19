import datetime

range_to_loop = range(5)

list_to_add_to = []

# for index in range_to_loop:
for index in range(5):
    # print(index)
    list_to_add_to.append(index)


print("Our resulting list")
print(list_to_add_to)

list_to_loop = [17, "moon", datetime.datetime(2023, 6, 7)]


list_to_add_to = []

for index in range(3):
    list_to_add_to.append(list_to_loop[index])

print("\nOur list of items pulled by index")
print(list_to_add_to)


list_to_add_to = []
for value in list_to_loop:
    list_to_add_to.append(value)

print("\nOur list of items pulled by value")
print(list_to_add_to)


list_of_numbers = [2, 3, 3, 5, 1, 2, 4, 3, 2, 9, 8]

filtered_list = []

for number in list_of_numbers:
    if number > 4:
        filtered_list.append(number)

print("\nOur filtered list")
print(filtered_list)


filtered_list_simplified = [number for number in list_of_numbers if number > 4]

print("\nOur filtered list simplified")
print(filtered_list)


string_to_split = "some,words,separated,by,commas"
list_from_split = string_to_split.split(",")
reconstructed_string = ""
capitalized_list = []

for word in list_from_split:
    reconstructed_string += word[0].capitalize() + word[1:] + ","
    capitalized_list.append(word[0].capitalize() + word[1:])

print("\nOur string with capitalized first letters of each word")
print(reconstructed_string)
print(str.join(",", capitalized_list))
