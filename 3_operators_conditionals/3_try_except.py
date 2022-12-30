
# my_conditional_result = 5 == 5
# my_conditional_result = 5 == 4 + 1
# my_conditional_result = 5 == 4
# my_conditional_result = 5 != 4
# my_conditional_result = 5 != 5
# my_conditional_result = not 5 == 4
# my_conditional_result = 5 > 4
# my_conditional_result = 5 <= 5
# my_conditional_result = 5 < 5

# my_conditional_result = not 5 > 4
# my_conditional_result = not 5 < 5
# my_conditional_result = not 5 <= 5

# my_conditional_result = "test" == "test"
# my_conditional_result = "test" == "Test"
# my_conditional_result = "teSt".lower() == "Test".lower()

try:
    # my_conditional_result = "teSt".lower() > 4
    my_conditional_result = "teSt".lower() == "Test".lower()
    print("\nThe result of my conditional")
    print(my_conditional_result)
except:
    print("An error occurred")
    
print("This is after the enclosed code block")