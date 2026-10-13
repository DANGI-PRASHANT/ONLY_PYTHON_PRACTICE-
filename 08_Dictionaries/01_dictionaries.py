student = {
    "Name": "Prashanta Basnet",
    "Age" : 18,
    "Location": "Tulsipur",
    "Gender": "Female"

}

for key in student:
    print(key)


for values in student.values():
    print(values)

for key,values  in student.items():
    print(f"{key}:{values}")

# checking key or value in Dictonary: 

if "Name" in student:
    print("Exists")

if "Prashanta Basnet"in student.values():
    print("Found")
else:
    print("Invalid")


# 