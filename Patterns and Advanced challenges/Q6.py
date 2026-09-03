# Write a program that goes through 'PYTHONPROGRAM', skips every 'O', and stops when it reaches 'G'.

words = "PROGRAMMING"

for ch in words:

    if ch == "O":
        continue
    if ch == "G":
        break
    print(ch)