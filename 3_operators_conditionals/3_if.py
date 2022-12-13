some_int = 2

# if 5 == 4:
if 5 == 5:
    some_int = 5
    print("The statement was true")
    print("\nThis line will only run when true")
elif some_int == 2:
    print("The some_int variable has a value of 2")
else:
    print("None of the previous statements are true")

print("\nThis line will run either way")
print(some_int)
