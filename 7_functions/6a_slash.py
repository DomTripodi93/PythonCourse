
def dynamic_param_func(show_message, message):
    if show_message:
        print(message)
    print("\n")

dynamic_param_func(message="some message", show_message=True)
dynamic_param_func(show_message=True, message="some message")
dynamic_param_func(True, "some message")


def positional_func(show_message, /, message):
    if show_message:
        print(message)
    print("\n")

# TypeError: positional_func() got some positional-only arguments passed as keyword arguments: 'show_message'
# positional_func(message="some message", show_message=True) 
# positional_func(show_message=True, message="some message")
positional_func(True, "some message")
positional_func(True, message="some message")


def positional_and_keywork_func(show_message, /, message, *, new_message):
    if show_message:
        print(message)
        print(new_message)
    print("\n")

# TypeError: positional_and_keywork_func() takes 2 positional arguments but 3 were given
# positional_and_keywork_func(True, "some message", "new message")
positional_and_keywork_func(True, "some message", new_message="new message")
positional_and_keywork_func(True, message="some message", new_message="new message")

