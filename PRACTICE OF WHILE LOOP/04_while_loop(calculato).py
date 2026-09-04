# Simple Calculator:

while True:

    num = input("Enter a Number_01 (or 'stop' to exist): ")

    if num.lower() == "stop":
        break

    num1 = float(num)
    operator = input("Enter operators (+ ,-,*,/): ")
    num2 = float(input("Enter a Number_02: "))

    if operator == "+":
        result = num1 + num2
        print(f"Sum of two number is {result}")
    elif operator == "-":
        result_01 = num1 - num2
        print(f"Substract of two number is {result_01}")

    elif operator == "*":
        result_02 = num1 * num2
        print(f"Multiplication of two number is {result_02} ")

    elif operator == "/":
        result_03 = num1 / num2
        print(f"Divided two number is {result_03}")
    else:
        print("Error")
        break

    

    
    

       


