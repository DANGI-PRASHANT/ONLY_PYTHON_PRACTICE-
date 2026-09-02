# Mixed challenge: For students = ['Ram', 'Sita', 'Hari'] and marks = [85, 39, 92], use range() to print name, mark,
 # and Pass/Fail:


students = ["Ram","Sita","Hari"]

marks = [85,39,92]

for i  in range(len(students)):
    print(f"Name: {students[i]}")
    print(f"Marks: {marks[i]}")


    if marks[i]>=40:
        print("Result: Pass")
    else:
        print("Result: Fail")

    print()