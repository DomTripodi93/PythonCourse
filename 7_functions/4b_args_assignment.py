
def capitalize_words(*args):
    result_string = ""
    for word in args:
        result_string += word[0].upper() + word[1:].lower() + " "
    return result_string.strip()

print(capitalize_words("any", "number", "of", "words"))
