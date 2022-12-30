
def print_arguments(arg_to_print, should_print=True):
    if (should_print):
        print(arg_to_print)
    return len(str(arg_to_print).split(" "))


count_words = print_arguments("Some message", False)

print("This is the returned value from print_arguments")
print(count_words)
print("\n")

print(print_arguments("Some other message"))
