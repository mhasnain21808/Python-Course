# DAY 12 WHILE LOOP

# 1 Basic while loop
i = 1
while i<=5:
    print(i)
    i +=1

# 2 Countdown
n=5
while n>0:
    print(n)
    n-=1


# 3 Ask user until valid input
num = ""
while not num.isnumeric():
    num=(input("Enter any value:"))
    print("Please Enter only no.")
print("Number Accepted:",num)


# 4 Loop through list using while
items = ["Apple","Banana","Grapes"]
i=0
while i <len(items):
    print(items[i])
    i+=1

# 5 Using Break
x = 1
while x <=10:
    if x == 5:
        break
    print(x)
    x +=1

# 6 Using Continue
y = 0
while y<10:
    y+=1
    if y%2 ==0:
        continue
    print(y)


# Password System
password = ""
attempts = 0

while password != "admin523" and attempts < 3:
    password=input("Enter your password:")
    attempts +=1
    if password == "admin523":
         print("Login successfully")
    else:
         print("Wrong password ,Try Again: Attempts counts:",attempts)
    if attempts ==3:
         print("Attempt Expired")

