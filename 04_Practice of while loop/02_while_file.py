# Keep asking for numbers. Print 'Greater than 100', 'Less than 100', or 'Equal to 100'. Stop
# with 'stop

while True:

    num = input("Enter a temperature (or 'stop' to exist): ")

    if num.lower() == "stop" :
        break

    num1 = float(num)
    if num1 >=30:
        print("Hot")
    elif num1 >=15:
        print("Normal")
    else:
        print("Cold")