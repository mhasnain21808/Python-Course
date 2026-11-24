# DAY 14 TUPLE

# Create tuple
fruit = ("Apple","Banana","Mango")
print(fruit)

# Indexing
print(fruit[0])
print(fruit[-1])

# # Slicing
nums = (10,20,30,40,50)
print(nums[1:4])

# Looping
Colors = ("Red","Blue","Green")
for c in Colors:
    print(c)

#Tuple Lenght
print(len(Colors))

#Concatenation
a = (1,2)
b = (3,4)
print(a+b)

#Packing and Unpacking
Data = ("Laptop",45000,"Black")
product , price , color = Data
print(f"product : {product} ,price :{price} , color:{color}")

# Nested Tuple inside list
employees = [("E101","Hamza","Chakwal"),("E102","Ali","Sialkot")]
for eid,name,city in employees:
    print(eid,name,city)