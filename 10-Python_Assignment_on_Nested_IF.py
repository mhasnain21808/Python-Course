# Assignment No. 1
Security_Code = int(input("Enter security code:"))
if Security_Code == 5566:
    Employee_Department = input("Enter your employee department:")
    if Employee_Department.lower() == "finance":
        Access_Level = int(input("Enter your Access level:"))
        if Access_Level == 5:
            print("Access granted:Welcome to the meeting room")
        else:
            print("Insufficent Access level")
    else:
        print("Access denied:Department not allowed")
else:
    print("Invalid Security code")


# Assignment NO. 2

Registration_no = int(input("Enter your registration no:"))
if Registration_no == 1221:
    Subject = input("Enter your subject name:")
    if Subject.lower() == "python":
        password = int(input("Enter your password:"))
        if password == 8888:
            print("Login successfully!Start your exam")
        else:
            print("Wrong password")
    else:
        print("Subject not available")
else:
    print("Registration failed")
