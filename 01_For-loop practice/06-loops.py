# Age checker using loops:

names = ["Ram","Sita","Hari"]

ages = [20,16,25]

for i in range(len(names)):
    print(f"Name:{names[i]}")
    print(f"Age: {ages[i]}")

    if ages[i] >=18:
        print("Adult")
    else:
        print("Minor")

    print()