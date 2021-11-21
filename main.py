# option 1 to open and read a file
# important to use close() with this option
# file = open("my_file.txt")
# contents = file.read()
# print(contents)
# file.close()

# option 2
# "with" keyword will manage file and close automaticlly
# modes
# 'r' -> read only
# 'w' -> write
# 'a' -> append
with open("my_file.txt", mode="w") as file:
    file.write("How's it going")

