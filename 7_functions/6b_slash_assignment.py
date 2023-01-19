
def capitalize_words(show_result, /, *, string_to_check):
    string_parts = str(string_to_check).split(" ")
    result_string = ""
    for word in string_parts:
        result_string += word[0].upper() + word[1:].lower() + " "
    if show_result:
        print(result_string.strip())
    return result_string.strip()


capitalize_words(True, string_to_check="some random string")
