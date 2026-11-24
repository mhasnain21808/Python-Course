# Day 17 Range + Loops

# print 1 to 5 
for i in range(1,6):
    print(i)

# Print Even numbers from 0 to 18

for i in range(0,19,2):
    print(i)

# Countdown from 10 to 1

for i in range(10,0,-1):
    print(i)

# Print loop through list using index
items = ["pen","Book","Laptop"]
for i in range(len(items)):
    print(i,items[i])


# Generate Employee IDs
for i in range(1,6):
    print("EMP:",i)

# Create years list
years = []
for i in range(2015,2025):
    years.append(i)
print(years)


# Clean city names using range
cities = ["ChaKwaL","SiaLKOt","RawaLPINDi"]
for i in range(len(cities)):
    cities[i]=cities[i].strip().title()
print(cities)


# Extract last 4 letters from IDs

ids = ["EMP--0001223","EMP--123589","EMP---13289"]
for i in range(len(ids)):
    print(ids[i][-4:])

for i in range(1,4):
    for j in range(1,4):
        print(i,j)