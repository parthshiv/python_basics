names = ["parth", "shital", "rahul"]

upper = [n.upper() for n in names]
print(upper)

squares = []
for i in range(1, 6):
    squares.append(i*i)

# this will do same as above in just one line by using list comprehension approach
squares = [i*i for i in range(1, 6)]
print(squares)

#list comprehension with if condition
evens = [i for i in range(10) if i % 2 == 0]
print(evens)

#list comprehension with if and else condition

labels = [f"{x}: Even" if x % 2 == 0 else f"{x}: Odd" for x in range(5)]
print(labels)