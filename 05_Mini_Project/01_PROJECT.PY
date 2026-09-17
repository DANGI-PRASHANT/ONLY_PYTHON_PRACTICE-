students  = ["Ram","Hari","Sita","Ankit"]
marks = [45,67,56,87]

for i,student in enumerate(students):

    print(f"{i+1}.Student: {students[i]}")
    print(f" Marks: {marks[i]}")
    

    if marks[i] >=40:
        print(f" Result: Pass")
    else:
        print(" Result: Fail")

    if marks[i] %2 ==0:
        print(f" {marks[i]} is even number.")
    else:
        print(f" {marks[i]} is odd number.")

    print()

    if marks[i] >= 80:
        print(f"                             Highest score is {marks[i]}                ")
    print()
