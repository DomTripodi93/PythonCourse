
def capitalize_words(**kwargs):
    result_string = ""
    for word in kwargs["word_list"]:
        result_string += word[0].upper() + word[1:].lower() + " "
    return result_string.strip()

print(capitalize_words(word_list  = ["my", "keyword", "list", "of", "words"]))
