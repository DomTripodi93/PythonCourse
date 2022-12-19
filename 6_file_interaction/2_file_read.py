
# file = open("new.txt", "w+")
file = open("new.txt", "a+")

# file.write("Some random text")
file.write("\nAnother line of text")


# file.flush()
# file.seek(0)

file.close()
file = open("new.txt")  # , "r")

print(file.read())
