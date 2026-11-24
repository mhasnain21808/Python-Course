# Day 13 List

# Create list
fruits = ["Apple","Banana","Grapes"]
print(fruits)

# Indexing
print(fruits[0])
print(fruits[-1])

# Update list
fruits[1]="Orange"
print(fruits)

#Add Items
fruits.append("Mango")
fruits.insert(1,"Papaya")
print(fruits)

#Remove Items
fruits.remove("Apple")
fruits.pop(2)
print(fruits)

#Slicing
nums =[10,20,30,40,50]
print(nums[0:3])
print(nums[-3:])

# Looping
for f in fruits:
     print("Fruit:",f)

# Replace wrong spellings
wrong = ["Chakwall","Sialkoot"]
fixed=[]
for c in wrong:
    c=c.replace("Chakwall","Chakwal").replace("Sialkoot","Sialkot")
    fixed.append(c)
print(fixed)
