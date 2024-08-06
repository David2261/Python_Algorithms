import sys

def sum(a, b):
	return a+b

if __name__ == '__main__':
	a, b = map(lambda x: int(x), sys.stdin.readline().split())
	print(sum(a, b))