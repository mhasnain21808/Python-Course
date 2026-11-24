# DAY 11 FOR LOOP

#1 Basic loop
for i in range(1,11):
    print(i)

# 2 print characters
word = "Python"

for alphabet in word:
    print(alphabet)

word2 = "SQL"
for j in range(1,11):
    print(word2)


#3 Loop through list
items = ["Pen","Book","Laptop"]
for item in items:
    print(item)


# 4 Even numbers
for n in range(2,21,2):
    print(n)

# 5 Total Calculation
marks = [78,77,82]
total = 0
for m in marks:
    total += m
print("Total =",total)


# 6 Clean city names
cities = ["   Chakwal","Rawalpindi   ","   sialkot"]
cleaned =[]
for c in cities:
    cleaned.append(c.strip().title())
print(cleaned)

# # 7 loop with if-else condition
nums = [3,5,12,9,18,17,44,98]
for o in nums:
    if o % 2==0:
        print(o,"is Even Number")
    else:
        print(o,"is Odd Number")


# # 8 loop with if-elif-else condition
nums = [3,14,2,10,18,4]
for n in nums:
    if n>10:
        print(n,"is greater than 10")
    elif n==10:
        print(n,"is equal to 10")
    else:
        print(n,"is less than 10")


# 9  Extract from last 4 digits
id = ["EMP-001122","EMP-00001247"]
for last4 in id:
    print(last4[-4:]) 