# Multiplication table Generator: 


num = int(input("Enter a number: "))

for i in range(1,num+1):
    for j in range(1,11):
        
        print(f"{i} x {j} = {i*j}")

    print()
