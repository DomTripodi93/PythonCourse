
def print_arguments(arg_to_print, should_print=True):
    if (should_print):
        print(arg_to_print)


print_arguments("Some message", True)
print_arguments("Some other message")
print_arguments("", False)
