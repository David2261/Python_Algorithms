# $1 lesson


def binary_search(list, item):
	# Вместо list подстваляется мое 1 значение, т.е.
	# my_list, а на место item => число
	low = 0
	high = len(list)-1
	# Диапазон от 0 до размера списка

	while low <= high:
		mid = int((low + high)/2)
		# Находим центр
		guess = list[mid]
		# Добавляем в список элемент mid
		if guess == item:
			return mid
		if guess > item:
			high = mid - 1
		else:
			low = mid + 1
	return None

my_list = [1, 3, 5, 7, 9]


print(binary_search(my_list, 3))
print(binary_search(my_list, 11))
