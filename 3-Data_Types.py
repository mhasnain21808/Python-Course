# learning data types in Python
# 7 data types

# text data type 1
# string

customer_name="Hasnain"
print("Customer name is :",customer_name)
print("customer data type is:",type(customer_name))


# text data type 2
# 2 Numeric Data type
# 2.1 Integer complete number

rating=4
order_quantity=3

print("rating data type:",type(rating))
print("order_quantity data type:",type(order_quantity))


# 2.2 float decimal number
order_amount=879.5
print("order_amount data type",type(order_amount))


# 2.2 complex number
a = 3+4j
print(type(a))


# 3 boolean  True/False
a=True
print("a",type(a))


# # 4 sequence
# # 4.1 List
cities=["Chakwal","Jhelum","Rawalpindi","Lahore",14]

print(cities)
print(type(cities))


# 4.2 Tuple
Dimension=(2,3,54)
print(Dimension)

print(type(Dimension))


# #4.3  Range
num = range(5)  # [0,1,2,3,4]  
print(list(num))

print(type(num))

days= range(1,31)
print(list(days))

# # 5. Dictionary(dict)
student={
    "age" : "18",
    "name" : "Hasnain",
    "city" : "Chakwal"
}
print(student)
print(type(student))

# 6.Set
number={1,2,2,3,4}

print(number)
print(type(number))


# 7. None data type  - No value
remarks=None
print(remarks,type(remarks))