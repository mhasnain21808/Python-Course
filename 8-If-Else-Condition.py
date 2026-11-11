# IF ELSE CONDITION

age=int(input("Enter your age:"))

if age>=18:
    print("Qualified for Voting")
else:
    print("Not qualified for Voting")


# Check discount
amount = 1500

if amount>=1000:
    print("You get a discount")
else:
    print("Not discount")



# # If-Elif-Else (For multiple conditions)

marks = int(input("Enter student's marks:"))

if marks>=90:
    print(" Grade A+")
elif marks>=80:
    print("Grade A")
elif marks>=70:
    print("Grade B")
elif marks>=60:
    print("Grade C")
elif marks>=50:
    print("Grade D")
elif marks>=40:
    print("Grade E")
else:
    print("Fail")


# Sales Performance

sales = int(input("Enter your sales:"))

if sales>=100000:
    print("Higher performance")
elif sales>=50000:
    print("Medium performance")
else:
    print("Lower performance")


#String comparison Example

city = "Chakwal"
if city.lower() == "chakwal":
    print("City matched")
else:
    print("Not matched")

#Password Program
password = input("Enter your password:")
if password == "Admin":
    print("Successfully login")
else:
    print("Wrong password")

#Email validation
email = "username@gmail.com"
if "@" in email and "." in email:
    print("Valid Email")
else:
    print("Invalid Email")


# # Advanced Missing Data Check
value = ""
if value=="":
    print(" Missing Data Found")
else:
    print("Data Available")
