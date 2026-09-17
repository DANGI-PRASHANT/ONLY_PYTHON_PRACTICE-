# Pass or Fail:

while True:

    num= input("Enter a marks ( or 'stop' to exist): ")


    if num.lower() == "stop":
        break


    marks=float(num)

    if marks >=90:
        print("Congrulation")
        print("You got A+")
    elif marks >=80:
        print("Congrulation")
        print("You got A")
    elif marks >=70:
        print("Congrulation")
        print("You got B+")
    elif marks >=60:
        print("Congrulation")
        print("You got B")
    elif marks >=50:
        print("Congrulation")
        print("You got C+")
    elif marks >=40:
        print("Congrulation")
        print('You got C')
    elif marks >=35:
        print("Congrulation")
        print("You got D")
    else:
        print("Failed")