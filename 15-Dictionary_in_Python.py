# DAY 15 DICTIOARY

Student = {"Name":"Ali","Age":"18","City":"Chakwal"}
print(Student)

# # Accessing values
print(Student["Name"])
print(Student["City"])

# #Adding and Updating
Student["Marks"] = 85
Student["City"] = "Rawalpindi"
print(Student)

# # Removing
Student.pop("Age")
print(Student)

# Dictionary Methods
print(Student.keys())
print(Student.items())
print(Student.get("Name"))

# #Looping
for k in Student:
    print(k,Student[k])

# Nested Dictionary
employees ={
       "E101" : {"Name":"Ahmad","City":"Rawalakot"},
      "E102" : {"Name":"Amjad","City":"Rawalpindi"}
}

print(employees["E101"]["Name"])

# Mapping Wrong to Correct
mapper={
    "Chakwall" :"Chakwal",
    "Pindi" : "Rawalpindi"
}
print(mapper["Pindi"])