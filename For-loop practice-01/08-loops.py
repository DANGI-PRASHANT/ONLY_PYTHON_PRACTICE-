# Divisible by 5 :

names = ["A","B","C","D"]
numbers = [10,12,25,33]

for i in range(len(names)):
    print(f"Name: {names[i]}")
    print(f"Numbers: {numbers[i]}")

    if numbers[i] % 5==0:
        print("Divisible by 5")
    else:
        print("Not divisible by 5")
    print()