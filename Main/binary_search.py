
DB = [45, 23, 324, 54, 234, 43, 12, 'hello', 52, 19, 20, 10]


def binary_search(arr, element):
	left = 0
	right = len(arr) - 1
	index = -1
	while (left <= right) and (index == -1):
		mid = (left + right) // 2
		if arr[mid] == element:
			index = mid
		else:
			if element < arr[mid]:
				right = mid - 1
			else:
				left = mid + 1
	return index

print(binary_search(DB, 'hello'))