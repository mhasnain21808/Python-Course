# Day 16 SETS IN PYTHON

# Create set 
fruits = {"Apple","Banana","Apple","Mango"}
print(fruits)

# Add items

fruits.add("orange")
print(fruits)

#Remove items
fruits.discard("Banana")
print(fruits)


#Set operations
a = {1,2,3}
b = {3,4,5}

print("Union:",a|b)
print("Intersection:",a & b)
print("Difference:",a - b)
print("Symmetric Difference:",a ^ b)


# Remove Duplicates
cities = ["Chakwal","Rawalpindi","Sialkot","Chakwal"]
print(cities)
unique = set(cities)
print("unique cities",unique)

# Missing values
list1 = {"SQL","Excel","Power BI"}
list2 = {"SQL","Power BI"}
missing = list1-list2
print("Missing:",missing)


# Common Skills

deptA = {"SQL","Excel","Python"}
deptB = {"Excel","Python","Power BI"}
print("Common Skills:",deptA & deptB)