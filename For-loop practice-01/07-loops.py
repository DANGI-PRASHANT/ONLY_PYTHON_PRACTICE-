# Salary checker using loop and if-else condition:

employees = ["Ram","Sita","Hari"]
salaries = [50000,30000,60000]

for i in range(len(employees)):
    print(f"Employees: {employees[i]}")
    print(f"Salary:{salaries[i]}")

    if salaries[i] >=50000:
        print("High salary")
    else:
        print("Normal salary")
    print()