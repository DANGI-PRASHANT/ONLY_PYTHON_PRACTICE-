

students = ["Alex","leo",'sita',"gita"]

for index,student in enumerate(students,1):

    if student == "Alex":
        continue

    if student == "leo":
        print("Pass")
    else:
        print("Checking...")

    if student == "sita":
        break

    print()
