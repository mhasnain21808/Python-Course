# 9- NESTED IF AND MULTIPLE CONDITIONS

print("Check your eligibility")

age = int(input("Enter your age:"))

if age>=18:
    id_no = int(input("Enter Your Id card no:"))
    if id_no == 1737:
        print("👍 You can enter")
    else:
        print("Wrong ID")
else:
    print("You are under age")

# Multiple Conditions(AND)

age = int(input("Enter your age:"))
Residence= input("Are you Pakistani:")

if age >= 18 and Residence.lower()=="yes":
    print("Eligible for driving license")
else:
    print("Not eligible for driving license")


# Multiple Conditions(OR)

age = int(input("Enter your age:"))
Residence= input("Do you have license:")

if age >= 18 or Residence.lower()=="yes":
    print("Eligible to drive")
else:
    print("Not eligible for drive")

