my_first_int = 1
# Used to grow to a max 64 bit value
#-9223372036854775808 - 9223372036854775807
# Now unbound the value of a python int will continue to 128, 256, and even 512 bits

print("Type of whole number")
print(type(my_first_int))


# 64 bit value - sometimes rounded because accuracy requires 128 bit value
my_first_float = 1.1
# Commonly reffered to as a double in other languages, where a float is only 32 bits

print("\nType of decimal number")
print(type(my_first_float))

print("\nFloat Accuracy Issue Example: .751 - .75")
print(.751 - .75)
