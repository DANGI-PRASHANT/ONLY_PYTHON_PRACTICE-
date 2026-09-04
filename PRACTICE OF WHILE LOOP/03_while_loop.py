# Login system: 



while True:
    username = input("Enter a username: ")
    password = input("Enter a password: ")

    if username == "admin" and password == "1234":
        print("Login sucessfull...!!")
        break
    else:
        print("Incorrect username or password . Try again")