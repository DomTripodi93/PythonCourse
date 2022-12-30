
def dynamic_callback_func(callback):
    print("this is the root function")
    callback()


def callback_func():
    print("this is the callback")


dynamic_callback_func(callback_func)
