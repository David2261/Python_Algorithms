

def sum(a, b):
	return a+b

if __name__ == '__main__':
	with open('input.txt', 'r') as file:
		line = file.readline()
		a, b = map(int, line.split())
	o = open('output.txt', 'w')
	o.write(str(sum(a, b)))