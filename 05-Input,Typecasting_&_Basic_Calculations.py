#Input and typecastingcls

name = input("Enter your name:")
print("Welcome ",name)

age=int(input("Enter your age:"))
age +=5
print("Your age is :",age)
print(type(age))

temperature = float(input("Enter today's temperature:"))
print(type(temperature))

# #Convert number to string
sales = 50000
text = "Total Sales;" + str(sales)
print(text)

# #Total sales calculator
product = input("Product name:")
quantity = int(input("Enter quantity sold:"))

price_per_unit = float(input("Enter price per unit:"))
total_sales = quantity * price_per_unit 

print("____________________")
print("Product name is :",product)
print("Total sales = ",total_sales)



num1 =int(input("Enter your 1st number:"))
num2 = int(input("Enter your 2nd num:"))

sum = num1 + num2
print(sum)


# #Assignment no 1
Employee = input("Enter employee name:")
Basic_salary = int(input("Enter basic salary:"))
Bonus_amount = int(input("Enter bonus amount:"))
Tax_percentage = float(input("Enter tax percentage:"))

Gross_salary = Basic_salary + Bonus_amount
Tax_amount = (Gross_salary * Tax_percentage)/100
Net_salary = Gross_salary - Tax_amount


print("Total salary of",Employee,"is",Net_salary)

#Assignment no 2
Student_name = input("Enter student name:")
Obtained_marks =float(input("Enter obtained marks of student:"))

Total_marks = float(input("Enter total marks:"))

Percentage = (Obtained_marks * 100)/Total_marks
print("Percentage of student is :",Percentage)
