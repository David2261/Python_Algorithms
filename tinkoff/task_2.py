n = int(input())
data = list(map(int, input().split()))

for i in range(n):
	if data[i] == -1:
		continue
	for j in range(i + 1, n):
		if data[j] != -1 and data[i] > data[j]:
			print("NO")
			exit()

print("YES")
for i in range(n):
	if data[i] != -1:
		print(data[i], end=" ")