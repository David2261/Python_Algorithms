def is_prime(n):
	"""проверка простоты числа"""
	if n < 2:
		return False
	for i in range(2, int(n**0.5) + 1):
		if n % i == 0:
			return False
	return True

def count_divisors(n):
	"""счетчик делителей"""
	count = 0
	for i in range(1, int(n**0.5) + 1):
		if n % i == 0:
			if n // i == i:
				count += 1
			else:
				count += 2
	return count

def count_composite_numbers(l, r):
	"""счетчик составных чисел с простыми делителями"""
	count = 0
	for num in range(l, r + 1):
		if not is_prime(num):
			divisor_count = count_divisors(num)
			if is_prime(divisor_count):
				count += 1
	return count

l, r = map(int, input().split())

print(count_composite_numbers(l, r))