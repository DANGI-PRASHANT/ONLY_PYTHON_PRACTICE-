
# NUMBER EXPLORER: 

numbers = [1,2,3,4,5,6,7,-8,9,10,-11,12,13,14,-15,16,17,-18,19,20]

for index,num in enumerate(numbers):

    if num <0:
        continue
    print(f" {num}")

    if num %2 ==0:
        print(f"  Even")
    else:
        print(f"  Odd")
    print()