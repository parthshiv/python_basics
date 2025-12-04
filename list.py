names = ["Apple", "Orange",  "Parth"]
names[2] = "Shivu"
# print(names[1])
# print(names[1:6])

# methods of list
names.append("Test_Append")
# print(names)
# print(names.index("orange"))
ornageIndex = names.index("Orange");
names.insert(ornageIndex,"InsertTest")
names.sort()

print("Assending Order: ",names)
names.sort(reverse=True)
print("Descending Order: ",names)
#names.pop(2)

#names.remove("Test_Append")
#print(names)
indexPop = names.index("Test_Append")
if indexPop >= 0 :
    names.pop(indexPop)
print("After deleting the indexed node : ",names)
names.remove("Apple")
print("After deleting the key node : ",names)
    

