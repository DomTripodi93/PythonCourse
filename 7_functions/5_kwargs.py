
# def add_number_list(*args):
#     result_sum = 0
#     for number in args:
#         result_sum += number
#     return result_sum


# # list_of_numbers = [3, 4, 5, 1, 2, 3]

# print(add_number_list(3, 4, 5, 1, 2, 3))

def commonly_edited_function(**kwargs):
    if "show_message" in kwargs.keys() and kwargs["show_message"]:
        print(kwargs["message"])
    elif not "show_message" in kwargs.keys():
        print("No show_message key")
    else:
        print("show_message is False")

        
    if "new_message" in kwargs.keys() and kwargs["show_new_message"]:
        print("new message")
        print(kwargs["new_message"])
    elif not "show_new_message" in kwargs.keys():
        print("No show_new_message key")
    else:
        print("show_new_message is False")
    
    print("\n")


commonly_edited_function(show_message=True, message="Some message")
commonly_edited_function(show_message=False, message="Some message")
commonly_edited_function(message="Some message")
commonly_edited_function(show_new_message=True, new_message="Some new message")
