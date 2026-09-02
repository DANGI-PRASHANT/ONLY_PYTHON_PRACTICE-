# For numbers = [10, 15, 20, 25, 30], use enumerate() and print only the index and value of even numbers.

numbers = [10,15,20,25,30]

for index,num in enumerate(numbers,1):
    if num %2 ==0:
        print(f"{index}.{num} = Even")