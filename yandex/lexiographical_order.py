def find_prefix_range(words, prefix):
	"""
	Найти диапазон слов, начинающихся с данного префикса в отсортированном списке слов.
	Возвращает кортеж (start, end), где start и end - индексы в списке слов.
	"""
	from bisect import bisect_left, bisect_right
	
	# Найти начальный индекс (первая позиция, где префикс >= prefix)
	start = bisect_left(words, prefix)
	
	# Найти конечный индекс (первая позиция, где префикс > prefix + '\x7f')
	end = bisect_left(words, prefix + chr(255))
	
	return (start, end)

if __name__ == '__main__':
	import sys
	input = sys.stdin.read
	data = input().splitlines()
	
	N, Q = map(int, data[0].split())
	words = data[1:N+1]
	queries = data[N+1:N+1+Q]
	
	results = []
	
	for query in queries:
		k, prefix = query.split()
		k = int(k)
		
		start, end = find_prefix_range(words, prefix)
		if start < end:
			# Общее количество слов с данным префиксом
			num_words = end - start
			if 1 <= k <= num_words:
				results.append(str(start + k))
			else:
				results.append("-1")
		else:
			results.append("-1")
	
	print("\n".join(results))
