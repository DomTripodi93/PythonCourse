some_int = 2

# if test := 5 == 5:
if (test := 5) == 5:
    some_int = test
    print("The statement was true")
    print("\nThis line will only run when true")

print("\nThis line will run either way")
print(some_int)
print(test)
