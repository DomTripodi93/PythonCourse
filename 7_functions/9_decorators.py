
def simple_double_dynamic_func(callback):
    def inner_func():
        print("This is the inner function")
        callback()
    return inner_func


def callback_func():
    print("This is the callback")


returned_function = simple_double_dynamic_func(callback_func)
print("The function that was returned")
print(returned_function)

print("\nCalling returned_function")
returned_function()

print("\nCalling simple_double_dynamic_func's result directly")
simple_double_dynamic_func(callback_func)()


#Our Decorated function acts like the result of the decorator 
## as if our function was passed as a callback
## simple_double_dynamic_func(decorated_callback_func)

#Calling our decorated function does the same as calling 
## inner_func where 
@simple_double_dynamic_func
def decorated_callback_func():
    print("This is the decorated callback")


print("\nWhat happens when we call decorated_callback_func")
decorated_callback_func()
