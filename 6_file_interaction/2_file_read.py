
# file = open("new.txt", "w")
# file = open("new.txt", "a")
# file.close()
# file = open("new.txt", "r")
# file = open("new.txt")


# file = open("new.txt", "w+")
file = open("new.txt", "a+")

file.write("\nSome new line of text - new number 2")

file.flush()
file.seek(0)

print(file.read())
