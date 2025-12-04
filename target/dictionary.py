# studentDetails = {
#     "marks": {
#         "Parth": 75,
#         "Shivu": 95,
#         "Test": 35
#         },
#     "attendance": {
#         "Parth": "70%",
#         "Shivu": "97%",
#         "Test": "30%"

#     }

# }
studentMarksDetails = {
   
        "Parth": 75,
        "Shivu": 95,
        "Test": 35
   

}
print(studentMarksDetails)
print(studentMarksDetails.items()) # returns items of disctionary/json object
print(studentMarksDetails.keys()) #returns keys
print(studentMarksDetails.values()) #returns values
studentMarksDetails.update({"Parth": 100, "Shivansh": 99}) # updates existing element and/or add new if not exists
#print(studentMarksDetails)

# below is the diff between get and [] of printing disctionary/json object in python
print(studentMarksDetails.get("Parth1")) # returns 100 if matches, if not then returns 'None'
print(studentMarksDetails["Parth1"]) # returns 100 if matches, if not then returns error
# but the diff is when the key not exists, get() will return 'None' while [] will returns an error
