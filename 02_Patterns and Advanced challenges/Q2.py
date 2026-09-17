# Write a nested loop to print a decreasing star pattern with 5 rows.

for i in range(5,0,-1):
    for j in range(1,i+1):
        print("*",end=" ")
    print()