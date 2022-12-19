# my_conditional_result = 5 == 5
# my_conditional_result = 5 == 4 + 1
# my_conditional_result = 5 == 4
# my_conditional_result = 5 != 4
# my_conditional_result = not 5 == 4
# my_conditional_result = 5 > 4
# my_conditional_result = 5 > 5
# my_conditional_result = 5 >= 5
# my_conditional_result = 5 <= 5
# my_conditional_result = 5 < 5
# my_conditional_result = 5 < 6
# my_conditional_result = 5 < 6 and 6 < 8
# my_conditional_result = not 5 > 6 and 6 < 8
# my_conditional_result = not 5 > 6 and not 6 < 8
# my_conditional_result = not 5 > 6 or not 6 < 8
# my_conditional_result = "test" == "test"
# my_conditional_result = "test" == "Test"
# my_conditional_result = "test" != "Test"
# my_conditional_result = "teSt".lower() == "TEsT".lower()
try:
    my_conditional_result = "teSt".lower() > 7
    print("\nConditional statement result")
    print(my_conditional_result)
except:
    print("The items are not comparable")