f = open("testfile.txt", "w") # this will open file for write mode
f.write("hello world \n my name is parth. \n it is my first python program")
f.close()
f = open("testfile.txt") # this will open file for read mode
#print(f.read())
# lines = f.readlines()
# print(lines)


line1 = f.readline()
line2 = f.readline()
line3 = f.readline()
# print(line1)
# print(line2)
# print(line3)
# f.close()

# same way to use With statemen to operate files functions

with open("testfile.txt") as f:
    print(f.read());
