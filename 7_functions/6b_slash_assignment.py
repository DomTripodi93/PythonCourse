
def capitalize_words(words_to_capitalize, /, **kwargs):
    string_parts = kwargs["string_to_check"].split(" ")
    result_string = ""
    words_capitalized = 0
    for word in string_parts:
        if (words_capitalized < words_to_capitalize):
            result_string += word[0].upper() + word[1:].lower() + " "
        else:
            result_string += word + " "
        words_capitalized += 1
    return result_string.strip()
    