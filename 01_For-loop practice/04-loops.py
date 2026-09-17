# For names = ['Ram', 'Sita', 'Hari', 'Gita'], print only names at even indexes.

names = ["Ram","Sita","Hari","Gita"]

for index,name in enumerate(names,1):
    if index %2 ==0:
        print(index,name)