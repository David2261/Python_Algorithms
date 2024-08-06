
def intersects(a, b):
	a1, b1 = a
	a2, b2 = b
	return not (b1 < b2 and a1 < a2 or b2 < b1 and a2 < a1)

def count_non(N, segments):
	count = [0] * N

	for i in range(N):
		for j in range(i + 1, N):
			if intersects(segments[i], segments[j]):
				count[i] += 1
				count[j] += 1


	print(sum(1 for c in count if c == 0))

if __name__ == '__main__':
	N = int(input())
	segments = [tuple(map(int, input().split())) for _ in range(N)]
	count_non(N, segments)