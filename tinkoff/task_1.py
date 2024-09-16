def res_set(interval_string):
	intervals = interval_string.split(',')
	result = set()

	for interval in intervals:
		if '-' not in interval:
			result.add(int(interval))
		else:
			start, end = map(int, interval.split('-'))
			result.update(range(start, end + 1))

	return ' '.join(map(str, sorted(result)))

input_string = input()
print(res_set(input_string))