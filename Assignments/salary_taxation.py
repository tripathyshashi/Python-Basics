sal = int(input("Enter Salary: "))
if sal <= 30000:
    sal = sal - sal * (5 / 100)
    print("After taxation the salary is : ", sal)
elif sal > 30000 and sal <= 70000:
    sal = sal - sal * (15 / 100)
    print("After taxation the salary is : ", sal)
elif sal > 70000:
    sal = sal - sal * (25 / 100)
    print("After taxation the salary is : ", sal)
