# set is not-repetive 
b = {1, 2, 3 ,4 ,5, 5, 5,5}
a = set() # this will create empty set, we cannot use a = {} to create empty set as it will create empyty disctionary/json object

print(b, type(b))
b.add(6)
print(b)
a.add(2) #adds new element in set
print(a)
b.remove(5) #removes element from set
print(b)

s1 = {1,2,3,4,11,12}
s2 = {5,6,7,8,2,4,9}
print("union: ", s1.union(s2)) # returns all combined 
print("intersection: ",s1.intersection(s2)) # returns common/same from both
print("difference: ", s1.difference(s2)) # returns unique from s1 which does not exists in s2
print(s1-s2) # same like difference method above
