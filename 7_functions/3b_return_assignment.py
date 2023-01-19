
def capitalize_words(string_to_check):
    string_parts = str(string_to_check).split(" ")
    result_string = ""
    for word in string_parts:
        result_string += word[0].upper() + word[1:].lower() + " "
    return result_string.strip()

print(capitalize_words("test sentence"))
