age=int(input("enter the age"))
mi=float(input("enter the monthly income"))
cs=int(input("enter the credit score"))
le=float(input("enter the amount of existing loan"))
if le>500000:
    print("reject loan beacause of existing loan")
else:
    if age>21 and age<60 and mi>30000 and cs>750:
        print("loan approved as eligibility is reached")
    elif cs>650 and cs<749:
        print("approved only if salary>60000")
    elif cs<650:
        print("rejected")
    else:
        print("rejected age not matched")       