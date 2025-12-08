def square(n):
    return n * n;

arr = [1,2,3,4,5] 

# example of map. Map used to take items, change/transform ALL of them 
a = map(square, arr);
print(list(a))

# example of filter. Filter used to take items and return ONLY matching/selective items, not all
def starts_with_p(name):
    return name.startswith("P")

names = ["Parth", "Shital", "Priya", "Rahul"]

result = list(filter(starts_with_p, names))

print(result)

