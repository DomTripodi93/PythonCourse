
def dynamic_nested_callback_func(callback):
    def nested_func():
        print("this is the nested function")
        callback()
    return nested_func


def callback_func():
    print("this is the callback")


# dynamic_nested_callback_func(callback_func)()
dynamic_nested_callback_func(lambda: print("this is the lambda callback"))()

# nested_func_result = dynamic_nested_callback_func(callback_func)

# nested_func_result()
