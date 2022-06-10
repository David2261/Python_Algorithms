n = int(input("n="))


for a in range(n+1):
    continue
lst = []
i = 2
while i <= n:
    if a[i] != 0:
        lst.append(a[i])
        for j in range(i, n+1, i):
            a[j] = 0
    i += 1
print(lst)