# Write a program that prints an increasing star pattern and then a decreasing star pattern, without repeating the
# middle row unnecessarily.



# INCREASING PATTERN: 

for i in range(1,6):
    for j in range(1,i+1):
        print("*",end=" ")
    print()

# DECREASING PATTER: 

for k in range(4,0,-1):
    for l in range(1,k+1):
        print("*",end=" ")
    print()