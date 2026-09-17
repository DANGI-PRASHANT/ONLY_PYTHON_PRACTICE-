# Write a nested loop that prints every pair (i, j) where i is 1–3 and j is 1–3, but skip pairs where i == j.

for i in range(1,5):
    for j in range(1,5):

        if i ==j:
            continue
        print(i,j)